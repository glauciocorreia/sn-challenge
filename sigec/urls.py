"""sigec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from clientes import urls as clientes_urls
from contas import urls as contas_urls
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import (
handler404, handler500
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include(clientes_urls)),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contas/', include('contas.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('', include('social_django.urls', namespace='social')),
]

handler404 = 'clientes.views.handler404'
handler500 = 'clientes.views.handler500'
