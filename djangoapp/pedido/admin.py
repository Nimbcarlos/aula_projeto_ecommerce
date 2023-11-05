from django.contrib import admin
from pedido.models import Pedido, ItemPedido

# Register your models here.

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'id', 'usuario', 'total', 'status',
    list_display_links = 'usuario',
    search_fields = 'id', 'usuario', 'status',
    inlines = ItemPedidoInline,

admin.site.register(ItemPedido)