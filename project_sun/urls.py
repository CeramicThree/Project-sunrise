"""project_sun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app_start import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/', include('allauth.urls')),
    path('sunriseproject/', admin.site.urls),
    path('metrostroi/news/', views.news, name="news"),
    path('metrostroi/servers/', views.servers, name="servers"),
    path('metrostroi/requests/', views.requests, name="requests"),
    path('metrostroi/complaint/', views.complaints, name="complaints"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
