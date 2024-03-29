"""Esame_Linguaggi_Dinamici URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth import login
from . import views

urlpatterns = [
    # path('login/', login, {'template_name': 'Login.hrml'}, name='login'),
    path('Campionato/', views.mainpage, name='index'),
    url(r'^register/', views.SignUp.as_view(), name='register'),
    url(r'^logout/', views.logoutuser, name='logoutuser'),
    url(r'^Campionato/', include(('Campionato_Calcio.urls', 'Campionato_Calcio'), namespace="Campionato_Calcio")),
    url(r'^', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
