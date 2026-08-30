from django.urls import path
from core.views import criar_tarefa, index, lista_tarefas, editar_tarefa, deletar_tarefa

urlpatterns = [
    path('', index, name='index'),
    path('tarefas/', lista_tarefas, name='tarefas'),
    path('cadastro/', criar_tarefa, name='criar_tarefa'),
    path('deletar/<int:id>/', deletar_tarefa, name='deletar_tarefa'),
    path('editar/<int:id>/', editar_tarefa, name='editar_tarefa')
]
