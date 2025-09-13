from django.urls import path
from .views import CachorroCreateView,CachorroListView,CachorroUpdateView,CachorroDeleteView

app_name = 'cadastrar_cachorro'

urlpatterns = [
    
    path('<int:pk>/', CachorroListView.as_view(), name='listar_cachorros'),
    path('criar/<int:pk>/', CachorroCreateView.as_view(), name='criar_cachorro'),
    path('atualizar/<int:pk>/', CachorroUpdateView.as_view(), name='atualizar_cachorro'),
    path('deletar/<int:pk>/', CachorroDeleteView.as_view(), name='deletar_cachorro'),
]