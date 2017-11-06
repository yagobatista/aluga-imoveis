# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aluguel.models import Aluguel
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile


# Register your models here.
class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(150, 150)]

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.imagem))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

class AluguelAdmin(admin.ModelAdmin):
     # Remove the delete Admin Action for this Model
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(AluguelAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


    readonly_fields = ('nome','telefone','imagem','rua','numero','cidade','bairro','valor','foto',)
    fields = ('nome','telefone','rua','numero','cidade','bairro','valor','foto',)
    list_display = ('rua','numero','cidade','bairro','foto',)
    foto = AdminThumbnail(image_field=cached_admin_thumb)
    foto.short_description = 'Image'

admin.site.register(Aluguel,AluguelAdmin)
