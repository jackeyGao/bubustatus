# -*- coding: utf-8 -*-
'''
File Name: bubustatus/api.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 六  9/12 21:02:33 2015
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from bubustatus.serializers import StepSerializer
from bubustatus.serializers import LabelSerializer
from bubustatus.models import Step
from bubustatus.models import Label


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)
