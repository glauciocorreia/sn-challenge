from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Cliente(models.Model):
  nome = models.CharField(max_length=150, null=False, blank=False)
  telefone = PhoneNumberField(null=False, blank=False, unique=True)
  endereco = models.CharField(max_length=200, null=False, blank=False)
  numero = models.CharField(max_length=15, null=True, blank=True)
  cidade = models.CharField(max_length=80, null=False, blank=False)
  estado = models.CharField(max_length=80, null=False, blank=False)
  pais = models.CharField(max_length=80, null=False, blank=False)
  cep = models.IntegerField(null=False, blank=False)
  

  def __str__(self):
      return self.nome 
  