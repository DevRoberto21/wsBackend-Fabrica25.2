from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Pessoa
from .forms import PessoaForm

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "criar_pessoa.html"
   
    def get_success_url(self):
        return reverse_lazy('cachorros:criar_cachorro', kwargs={'pk': self.object.pk})

class PessoaListView(ListView):
    model = Pessoa
    template_name = "listar_pessoas.html"
    context_object_name = "pessoas"

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "criar_pessoa.html"
    context_object_name = "pessoa"
    success_url = reverse_lazy('cadastrar_pessoa:listar_pessoas')

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'deletar_pessoa.html'
    context_object_name = 'pessoa'
    success_url = reverse_lazy('cadastrar_pessoa:listar_pessoas')

class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'detalhes_pessoa.html'
    context_object_name = 'pessoa'