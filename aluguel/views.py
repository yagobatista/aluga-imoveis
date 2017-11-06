# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render,redirect
from aluguel.models import Aluguel
from aluguel.forms import AluguelForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    lista = Aluguel.objects.all()
    return render(request,'aluguel/index.html',{'lista': lista})


def pesquisa(request):
    filters = None
    vals = {}
    if 'bairro' in request.GET:
        filters =  Q(bairro__contains = request.GET['bairro'])
        vals['bairro'] = request.GET['bairro']
    if 'cidade' in request.GET:
        filters = filters & Q(cidade__contains = request.GET['cidade'])
        vals['cidade'] = request.GET['cidade']

    lista = Aluguel.objects.filter(filters)
    vals ['lista'] = lista
    return render(request, 'aluguel/index.html',vals )

def cadastro(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'aluguel/cadastro-sucesso.html')
        else:
            return render(request,'aluguel/cadastro.html',{'form': form})
    else:
        form = AluguelForm()
        return render(request,'aluguel/cadastro.html',{'form':form})
