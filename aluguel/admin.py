# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aluguel.models import Aluguel
# Register your models here.
class AluguelAdmin(admin.ModelAdmin):
     readonly_fields = ('nome','telefone','rua','numero','cidade','bairro',)

admin.site.register(Aluguel,AluguelAdmin)
