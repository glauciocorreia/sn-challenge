from django.shortcuts import render

def clientes_lista(request):
  return render(request, 'clientes.html')
