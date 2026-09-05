from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from core.forms import TarefaForm
from core.models import Tarefa

def index(request):
    return render(request, 'registration/login.html')

@login_required
def lista_tarefas(request):
    lista = Tarefa.objects.all()
    return render(request, 'core/tarefas.html', {'tarefas': lista})

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas')
        return render(request, 'core/criar_tarefa.html', {'form': form})
    return render(request, 'core/criar_tarefa.html')

@login_required
def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            return redirect('tarefas')
        return render(request, 'core/editar_tarefa.html', {'form': form, 'tarefa': tarefa})
    return render(request, 'core/editar_tarefa.html', {'tarefa': tarefa})

@login_required
def deletar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, 'core/deletar_tarefa.html', {'tarefa': tarefa})