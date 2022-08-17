from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # 用户界面
    path('index/', views.index),
    path('user/regis/', views.user_regis),

    # 发送短信
    path('send/code/', views.send_code),
]
