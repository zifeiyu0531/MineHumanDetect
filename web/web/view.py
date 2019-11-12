import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from . import control

BASE_DIR = settings.BASE_DIR

def text(request):
    return render(request, 'SystemControl.html')

def ajax_pic(request):
    result_list = {
        "src": "../static/images/img-text.jpg",
        "detected": 0,
        "num": 0
    }
    return HttpResponse(
        json.dumps(result_list),
        content_type='application/json'
    )