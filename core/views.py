from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from core.forms import TarefaForm
from core.models import Tarefa

@login_required
def index(request):
    lista = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'core/tarefas.html', {'tarefas': lista})

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            form.save()
            return redirect('index')
        return render(request, 'core/criar_tarefa.html', {'form': form})
    return render(request, 'core/criar_tarefa.html')

@login_required
def editar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            tarefa.save()
            return redirect('index')
        return render(request, 'core/editar_tarefa.html', {'form': form, 'tarefa': tarefa})
    return render(request, 'core/editar_tarefa.html', {'tarefa': tarefa})

@login_required
def deletar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('index')
    return render(request, 'core/deletar_tarefa.html', {'tarefa': tarefa})