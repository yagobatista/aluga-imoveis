# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Aluguel(models.Model):
    nome = models.CharField(max_length= 32 )
    telefone = models.CharField(max_length= 11 )
    rua = models.CharField(max_length= 250 )
    numero = models.IntegerField( )
    cidade = models.CharField(max_length= 250 )
    bairro = models.CharField(max_length= 250 )
    imagem = models.ImageField(upload_to='aluguel/')
    valor = models.IntegerField(default='0')
    def __str__(self):
        return self.nome;
