# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aluguel.models import Aluguel
# Register your models here.
class AluguelAdmin(admin.ModelAdmin):
     # Remove the delete Admin Action for this Model
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    def has_edit_permission(self, request, obj=None):
        return False
    def save_model(self, request, obj, form, change):
        #Return nothing to make sure user can't update any data
        pass
    readonly_fields = ('nome','telefone','imagem','rua','numero','cidade','bairro',)
    list_display = ('nome','telefone' , 'imagem')
admin.site.register(Aluguel,AluguelAdmin)
