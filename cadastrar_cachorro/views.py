import requests
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Cachorro
from .forms import CachorroForm
from cadastrar_pessoa.models import Pessoa


class CachorroCreateView(CreateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "criar_cachorro.html"  

    def get_success_url(self):
        return reverse_lazy("cadastrar_pessoa:detalhes_pessoa", kwargs={'pk': self.object.dono.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        context['dono'] = get_object_or_404(Pessoa, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        dono = get_object_or_404(Pessoa, pk=self.kwargs['pk'])
        form.instance.dono = dono
        return super().form_valid(form)


class CachorroListView(ListView):
     model = Cachorro
     template_name = 'listar_cachorros.html' 
     context_object_name = 'cachorros'

     def get_queryset(self):
        dono = get_object_or_404(Pessoa, pk=self.kwargs['pk'])
        return Cachorro.objects.filter(dono=dono)

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dono'] = get_object_or_404(Pessoa, pk=self.kwargs['pk'])
        return context


class CachorroUpdateView(UpdateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = 'criar_cachorro.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dono'] = self.get_object().dono
        return context
    
    def get_success_url(self):
        return reverse_lazy('cadastrar_pessoa:detalhes_pessoa', kwargs={'pk': self.object.dono.pk})


class CachorroDeleteView(DeleteView):
    model = Cachorro
    template_name = 'deletar_cachorro.html'
    
    def get_success_url(self):
        return reverse_lazy('cadastrar_pessoa:detalhes_pessoa', kwargs={'pk': self.object.dono.pk})