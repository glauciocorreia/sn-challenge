from django.urls import path
from .views import clientes_lista
from .views import clientes_novo
# from .views import clientes_atualizar
# from .views import clientes_excluir

urlpatterns = [
    path('lista/', clientes_lista, name="clientes"),
    path('novo/', clientes_novo, name="clientes_novo"),
    # path('cliente/atualizar/<int:id>', clientes_atualizar, name="clientes_atualizar"),
    # path('cliente/excluir/<int:id>', clientes_excluir, name="clientes_excluir"),
]
