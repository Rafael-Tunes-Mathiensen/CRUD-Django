from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    data = models.DateField(null=False)
    status = models.BooleanField(null=False)

    def __str__(self):
        return self.titulo