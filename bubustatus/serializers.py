# -*- coding: utf-8 -*-
'''
File Name: bubustatus/serializers.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 六  9/12 20:57:30 2015
'''

from rest_framework import serializers
from bubustatus.models import Label, Step


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
