from django.urls import path
from registro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listaralunos', views.listar_aluno, name='listaralunos'),
    path('createaluno', views.criar_aluno, name='criaraluno'),
    path('deletealuno/<int:aluno_id>', views.delete_aluno, name='deletealuno'),
    path('updatealuno/<int:aluno_id>', views.update_aluno, name='updatealuno'),

    path('listaraulas', views.listar_aula, name='listaraulas'),
    path('createaulas', views.criar_aula, name='criaraula'),
    path('deleteaula/<int:aula_id>', views.delete_aula, name='deleteaula'),
    path('updateaula/<int:aula_id>', views.update_aula, name='updateaula'),

    path('listarregistro', views.listar_registro, name='listarregistros'),
    path('createregistro', views.criar_registro, name='criarregistro'),
    path('deleteregistro/<int:registro_id>', views.delete_registro, name='deleteregistro'),
    path('updateregistro/<int:registro_id>', views.update_registro, name='updateregistro'),
    path('buscaregistro', views.busca_registro, name='buscaregistro'),
    path('registrarpresenca/<int:aula_id>', views.registrar_presenca, name='registrarpresenca'),
]