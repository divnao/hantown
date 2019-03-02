from django.conf.urls import url

from app1 import views

urlpatterns = [
    url('^$', views.welcome),
    url('^index/$', views.index),
]
