from django.urls import path
from .views import clientes_lista
from .views import clientes_novo
from .views import clientes_atualizar
from .views import clientes_excluir
from .views import clientes_localizacao

urlpatterns = [
    path('lista/', clientes_lista, name="clientes_lista"),
    path('novo/', clientes_novo, name="clientes_novo"),
    path('atualizar/<int:id>', clientes_atualizar, name="clientes_atualizar"),
    path('excluir/<int:id>', clientes_excluir, name="clientes_excluir"),
    path('localizacao/<int:id>', clientes_localizacao, name="clientes_localizacao"),
]

handler404 = 'clientes.views.handler404'
handler500 = 'clientes.views.handler500'
