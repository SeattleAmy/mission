from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^log$', views.log, name = 'log'),
    url(r'^rules$', views.rules, name = 'rules'),
    url(r'^admin$', views.admin, name = 'admin'),
    url(r'^submit$', views.submit, name = 'submit'),
    url(r'^reset$', views.reset, name = 'reset'),
    url(r'^success/(?P<id>\d+)$', views.success, name = 'success'),
    url(r'^reject/(?P<id>\d+)$', views.reject, name = 'reject'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^admin_index$', views.admin_index, name = 'admin_index'),
    url(r'^admin_login$', views.admin_login, name = 'admin_login'),
    url(r'^create_team$', views.create_team, name = 'create_team'),
    url(r'^submit_mission/(?P<id>\d+)$', views.submit_mission, name = 'submit_mission'),
    url(r'^create_mission$', views.create_mission, name = 'create_mission'),
    url(r'^admin_registration$', views.admin_registration, name = 'admin_registration'),

]
