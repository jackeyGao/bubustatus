# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import division

import copy
import arrow
from django.http import QueryDict, Http404
from django.core.exceptions import FieldError
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render_to_response

from bubustatus.models import Label
from bubustatus.models import Step


def group_list(list,block):
    return [ list[i:i+block] for i in range(0,len(list),block) ]


class StepListView(ListView):
    template_name = 'bubustatus/list.html'
    paginate_by = 25
    context_object_name = 'steps'
    queryset = Step.objects.order_by('-insert')

    def get_params(self):
        params = self.request.GET
        params = [(k, params.get(k)) for k in params  if k <> 'page' and \
                params.get(k)]
        query_dict = QueryDict('', mutable=True)
        query_dict.update(dict(params))
        return query_dict

    def get_context_data(self, **kwargs):
        context = super(StepListView, self).get_context_data(**kwargs)
        context["params"] = self.get_params()
        return context

    def get_queryset(self):
        params = self.get_params()
        try:
            queryset = Step.objects.filter(**params.dict()).order_by('-insert')
        except FieldError:
            queryset = Step.objects.order_by('-insert')

        return queryset


def labels(request):
    """列出所有label 标示每个label的step数
    
    :url:   ~/labels:   列出所有label 标示每个label的step数
    """
    steps = Step.objects.all()
    groups = group_list(Label.objects.all(), 6)
    
    return render_to_response('bubustatus/labels.html',locals())


def step(request, label, name):
    """查看某个step的详细数
    :url:   ~/step/<label>/<step>: 查看某个step的详细数
    """
    steps = Step.objects.filter(name=name, label=label).order_by('insert')

    if not steps:
        raise Http404(u"%s step没有找到, 请确认." % name)

    step_count = steps[0].label.step_count
    step_count = int((len(steps) + step_count - 1) / step_count) * step_count

    confirm_steps = steps.filter(is_confirm=True)
    progress = int(round(len(confirm_steps) / step_count, 2) * 100)
    step_status = list(set([ s.status for s in steps ]))

    start_time = arrow.get(steps.order_by('insert')[0].insert)
    end_time   = arrow.get(steps.order_by('-confirm_time')[0].confirm_time)
    diff_time = end_time - start_time

    return render_to_response('bubustatus/detail.html', locals())


def timeline(request):
    queryset = Step.objects.filter(label="gemini").order_by('-insert')[0:20]

    steps = []
    for step in queryset:
        if step.is_confirm:
            _step = copy.deepcopy(step)
            _step.action = "commit"
            _step.thetime = step.insert
            step.action = "confirm"
            step.thetime = step.confirm_time

            steps.append(_step)
            steps.append(step)
        else:
            step.thetime = step.insert
            steps.append(step)
        
    return render_to_response('bubustatus/timeline.html', locals())

