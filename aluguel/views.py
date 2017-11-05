# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from aluguel.forms import AluguelForm
# Create your views here.
def home(request):
    return render(request,'aluguel/index.html')
def cadastro_sucesso(request):
    return render(request,'aluguel/cadastro_sucesso.html')
def cadastro(request):
    form = AluguelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(cadastro_sucesso)
    return render(request,'aluguel/cadastro.html',{'form': form})
