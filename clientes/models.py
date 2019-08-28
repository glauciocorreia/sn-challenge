from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=80)
  telefone = models.CharField(max_length=15)
  endereco = models.CharField(max_length=100)
  numero = models.CharField(max_length=6)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=100)
  pais = models.CharField(max_length=50)
  cep = models.CharField(max_length=10)
  

  def __str__(self):
      return self.nome 
  