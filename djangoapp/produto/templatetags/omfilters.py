from django.template import Library
from utils import rands


register = Library()


@register.filter
def formata_preco(val):
    return rands.formata_preco(val)


@register.filter
def cart_total_qtd(carrinho):
    return rands.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return rands.cart_totals(carrinho)