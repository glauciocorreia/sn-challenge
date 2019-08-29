from django.urls import path

from . import views


urlpatterns = [
    path('cadastrar/', views.Cadastrar.as_view(), name='cadastrar'),
]