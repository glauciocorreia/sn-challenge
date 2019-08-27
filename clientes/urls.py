from django.urls import path
from .views import clientes_lista
from .views import clientes_novo
from .views import clientes_atualizar
from .views import clientes_deletar

urlpatterns = [
    path('lista/', persons_list, name="clientes_lista"),
    path('novo/', persons_new, name="clientes_novo"),
    path('atualizar/<int:id>', persons_update, name="clientes_atualizar"),
    path('excluir/<int:id>', persons_delete, name="clientes_deletar"),
]
