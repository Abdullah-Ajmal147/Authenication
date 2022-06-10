from django.contrib import admin
from django.urls import path
from Email_Verify import views


urlpatterns =[
    path('', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/token', views.token, name='token'),
    path('/success', views.success, name='success'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('/error', views.error, name='error'),
]