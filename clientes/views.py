from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def clientes_lista(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes.html', {'clientes': clientes})

def clientes_novo(request):
  form = ClienteForm(request.POST, None)

  if form.is_valid():
    form.save()
    return redirect('clientes')

  return render(request, 'clientes_novo.html', {'form': form})
