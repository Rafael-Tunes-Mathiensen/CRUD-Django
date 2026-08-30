from django.shortcuts import render
from core.models import Tarefa

def index(request):
    return render(request, 'core/index.html')

def lista_tarefas(request):
    lista = Tarefa.objects.all()
    return render(request, 'core/tarefas.html', {'tarefas': lista})