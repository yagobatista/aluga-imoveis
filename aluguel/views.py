# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'aluguel/index.html')
def cadastro(request):
    form = HabiliadeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'aluguel/cadastro.html',{'form': form})
