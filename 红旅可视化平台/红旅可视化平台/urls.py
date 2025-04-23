"""红旅可视化平台 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import RedirectView
from django.urls import path
from web.views import index, login, table, table_1, comment_cw, register, home, cor_analysis, table_2, qinggan_analysis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url='/login/')),
    path('index/',index),
    path('login/',login),
    path('table/',table),
    path('table_1/',table_1),
    path('comment_cw/',comment_cw),
    path('register/',register),
    path('index/',home),
    path('cor_analysis/',cor_analysis),

    path('qinggan_analysis/',qinggan_analysis),
    path('table_2/',table_2)
]
