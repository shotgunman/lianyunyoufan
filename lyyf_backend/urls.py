"""
URL configuration for lyyf_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lyyf import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),#用户信息
    path('site/<slug:slug>/', views.site),#景点
    path('restaurant', views.restaurant),#餐厅
    #path('login/', views.login),
    #path('where_to_go/', views.where_to_go),
    path('search_city/', views.search),#搜索城市
    #path('choice/<slug:slug1>/',views.choice),#出行天数
    #path('choice/<slug:slug1>/<slug:slug2>/', views.choice),#在意什么
    path('day_choose/',views.days_choose),
]
