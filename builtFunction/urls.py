from django.contrib import admin
from django.urls import path
from builtFunction import views


urlpatterns =[
    path('', views.register )
]