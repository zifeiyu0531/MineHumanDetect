from django.conf.urls import url

from . import view

urlpatterns = [
    url('SystemControl/', view.text),
    url(r'^ajax_pic/$', view.ajax_pic),
]