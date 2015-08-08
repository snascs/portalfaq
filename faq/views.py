from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from faq.models import Faq

class ListarFaq(ListView):
    model = Faq

class CriarFaq(CreateView):
    model = Faq
    fields = ['pergunta', 'resposta', 'data']
    success_url = reverse_lazy('faq:listar_faq')

class AlterarFaq(UpdateView):
    model = Faq
    fields = ['pergunta', 'resposta', 'data']
    success_url = reverse_lazy('faq:listar_faq')

class DeletarFaq(DeleteView):
    model = Faq
    fields = ['pergunta', 'resposta', 'data']
    success_url = reverse_lazy('faq:listar_faq')