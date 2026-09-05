from django.db import models
from django.conf import settings

class Tarefa(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    data = models.DateField(null=False)
    status = models.BooleanField(null=False)

    def __str__(self):
        return self.titulo