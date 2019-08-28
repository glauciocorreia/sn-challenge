from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm

@login_required
def clientes_lista(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def clientes_novo(request):
  form = ClienteForm(request.POST, None)

  if form.is_valid():
    form.save()
    return redirect('clientes_lista')

  
  setattr(request, 'title', 'novo')

  return render(request, 'clientes_form.html', {'form': form})

@login_required
def clientes_atualizar(request, id):
  cliente = get_object_or_404(Cliente, pk=id)
  form = ClienteForm(request.POST or None, instance=cliente)

  if form.is_valid():
    form.save()
    return redirect('clientes_lista')

  setattr(request, 'title', 'atualizar')
  
  return render(request, 'clientes_form.html', {'form': form})

@login_required
def clientes_excluir(request, id):
  cliente = get_object_or_404(Cliente, pk=id)
  form = ClienteForm(request.POST or None, instance=cliente)

  if request.method == 'POST':
    cliente.delete()
    return redirect('clientes_lista')
  
  return render(request, 'clientes_excluir.html', {'cliente': cliente})

@login_required
def clientes_localizacao(request, id):
  cliente = get_object_or_404(Cliente, pk=id)

  return render(request, 'clientes_localizacao.html', {'cliente': cliente})
