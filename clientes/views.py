from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def clientes_lista(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes.html', {'clientes': clientes})

def clientes_novo(request):
  form = ClienteForm(request.POST, None)

  if form.is_valid():
    form.save()
    return redirect('clientes_lista')

  return render(request, 'clientes_form.html', {'form': form})

def clientes_atualizar(request, id):
  cliente = get_object_or_404(Cliente, pk=id)
  form = ClienteForm(request.POST or None, instance=cliente)

  if form.is_valid():
    form.save()
    return redirect('clientes_lista')
  
  return render(request, 'clientes_form.html', {'form': form})
