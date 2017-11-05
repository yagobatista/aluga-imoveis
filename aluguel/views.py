# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from aluguel.models import Aluguel
from aluguel.forms import AluguelForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    lista = Aluguel.objects.all()
    return render(request,'aluguel/index.html',{'lista': lista})


def pesquisa(request):
    if 'q' in request.GET:
        q = request.GET['q']
        lista = Aluguel.objects.filter(bairro=q)
        return render(request, 'aluguel/pesquisa.html',
                      {'lista': lista, 'query': q})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)

def cadastro(request):
    form = AluguelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'aluguel/cadastro-sucesso.html')
    return render(request,'aluguel/cadastro.html',{'form': form})
