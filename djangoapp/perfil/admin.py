from django.contrib import admin
from perfil.models import Perfil

# Register your models here.

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = 'id', 'usuario', 'cpf',
    list_display_links = 'usuario',
    search_fields = 'id', 'usuario', 'cpf',
    list_per_page = 10
    ordering = '-id',