from django.shortcuts import redirect, render
from core.models import Tarefa

def index(request):
    return render(request, 'core/index.html')

def lista_tarefas(request):
    lista = Tarefa.objects.all()
    return render(request, 'core/tarefas.html', {'tarefas': lista})

def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = request.POST.get('status') == 'on'
        Tarefa.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)
        return redirect('tarefas')
    return render(request, 'core/criar_tarefa.html')

def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data = request.POST.get('data')
        tarefa.status = request.POST.get('status') == 'on'
        tarefa.save()
        return redirect('tarefas')
    return render(request, 'core/editar_tarefa.html', {'tarefa': tarefa})

def deletar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, 'core/deletar_tarefa.html', {'tarefa': tarefa})