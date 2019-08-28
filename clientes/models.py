from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
  nome = models.CharField(max_length=80)
  telefone = PhoneNumberField(null=False, blank=False, unique=True)
  endereco = models.CharField(max_length=100)
  numero = models.CharField(max_length=6)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=100)
  pais = models.CharField(max_length=50)
  cep = models.CharField(max_length=9)
  

  def __str__(self):
      return self.nome 
  