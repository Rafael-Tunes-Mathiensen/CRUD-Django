from django.urls import path
from core.views import index, lista_tarefas

urlpatterns = [
    path('', index, name='index'),
    path('tarefas', lista_tarefas, name='tarefas'),
]
