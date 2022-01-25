from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Categoria)
class CategoriaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Nivel)
class NivelProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Empresa)
class EmpresaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(TablaEscalacion)
class TablaEscalacionProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')