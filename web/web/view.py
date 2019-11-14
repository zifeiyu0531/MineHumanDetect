import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from . import control

BASE_DIR = settings.BASE_DIR

index = 1


def text(request):
    return render(request, 'SystemControl.html')

def ajax_pic(request):
    global index
    if index == 1:
        src = "../static/output/1.jpg"
        index = 2
    else:
        src = "../static/output/2.jpg"
        index = 1
    result_list = {
        "src": src,
        "detected": 0,
        "num": 0
    }
    return HttpResponse(
        json.dumps(result_list),
        content_type='application/json'
    )