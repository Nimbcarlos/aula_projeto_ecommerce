from django.contrib import admin
from produto.models import Produto, Variacao

# Register your models here.

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'get_preco_formatado', 'slug',
    list_display_links = 'nome',
    search_fields = 'id', 'nome', 'slug',
    inlines = VariacaoInline,