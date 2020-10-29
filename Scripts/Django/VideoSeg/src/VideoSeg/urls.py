from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^home', views.index, name='home'),
    url(r'^index', views.index, name='home'),
    url(r'^result', views.result, name='result')


]

urlpatterns += staticfiles_urlpatterns()
