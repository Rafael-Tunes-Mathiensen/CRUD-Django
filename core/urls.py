from django.urls import include, path
from core.views import criar_tarefa, index, editar_tarefa, deletar_tarefa

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', criar_tarefa, name='criar_tarefa'),
    path('deletar/<int:id>/', deletar_tarefa, name='deletar_tarefa'),
    path('editar/<int:id>/', editar_tarefa, name='editar_tarefa'),
    path('accounts/', include('django.contrib.auth.urls'))
]

