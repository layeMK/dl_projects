from django.urls import path
from django.conf.urls import url

from . import views

#app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    url('myposts/(?P<id>[0-9]+)', views.show, name='show')
]

