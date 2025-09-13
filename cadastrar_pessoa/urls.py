from django.urls import path
from .views import PessoaCreateView,PessoaListView,PessoaUpdateView,PessoaDeleteView,PessoaDetailView

app_name = 'cadastrar_pessoa'
urlpatterns = [
    path('', PessoaCreateView.as_view(), name='criar_pessoa'),
    path('listar_pessoa', PessoaListView.as_view(), name = 'listar_pessoas'),
    path('atualizar_pessoa/<int:pk>', PessoaUpdateView.as_view(), name= 'atualizar_pessoa'),
    path('deletar_pessoa/<int:pk>', PessoaDeleteView.as_view(), name= 'deletar_pessoa'),
    path('<int:pk>/',PessoaDetailView.as_view(), name='detalhes_pessoa'),
]