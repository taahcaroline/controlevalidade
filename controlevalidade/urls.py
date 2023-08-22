from django.urls import path
from controlevalidade import views


urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('sobre/', views.sobre, name='sobre'),
    path('caditens/', views.vagascad, name='caditens'),
    path('listaitens/', views.vagas, name='listaitens'),
    path('listaitens/<int:id>', views.vagasview, name='demandasview'),
    path('editaritens/<int:id>/', views.edititens, name='editaritens'),
    path('deletaritens/<int:cadastroitens_pk>/', views.itensdelete, name='deletaritens'),
    path('busca/', views.busca, name='busca'),
    # path('resultados/', resultados, name='resultados'),

    # path('clientescadastrados/', views.listaclientes, name='clientes'),
    # path('deletarcliente/<int:pk>/', views.deleteclientes, name='deletarcliente'),

    
]
