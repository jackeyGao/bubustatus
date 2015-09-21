# -*- coding: utf-8 -*-
'''
File Name: templatetags/in_label.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 六  9/12 14:20:55 2015
'''
import sys
import re
import arrow
from django import template

reload(sys)
sys.setdefaultencoding('utf-8')


register = template.Library()


@register.filter
def in_label_name(steps, label_name):
    return steps.filter(label__name=label_name)


@register.filter
def cut_string(string, need_length=5):
    length = 0
    r_string = ''

    for single_string in string.decode('utf-8'):
        if u'\u4e00' <= single_string <= u'\u9fff':
            length += 2
        else:
            length += 1

        if length > need_length:
            return r_string + '..'

        r_string += single_string
    
    return string

@register.filter
def humanize(datetime):
    return arrow.get(datetime).humanize()


@register.filter
def get_url(text):
    urlre = re.compile('href="(.*?)"')
    urls = re.findall(urlre,text)
    if urls:
        return urls[0]

    return None
