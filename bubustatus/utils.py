# -*- coding: utf-8 -*-
'''
File Name: bubustatus/utils.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 一  9/14 12:51:37 2015
'''
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response
