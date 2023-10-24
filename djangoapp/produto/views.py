from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

from . import models
from perfil.models import Perfil

PER_PAGE = 9

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = PER_PAGE
    ordering = ['-id']

class Busca(ListaProdutos):
    pass

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    pass

class RemoverDoCarrinho(View):
    pass

class Carrinho(View):
    pass

class ResumoDaCompra(View):
    pass