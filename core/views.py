from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def lista_tarefas(request):
    return render(request, 'core/tarefas.html')