from django.conf import settings
from django.db import models

# Create your models here.
class Aula(models.Model):
    aula = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.aula}"

class Agenda(models.Model):
    data_aula = models.DateField(default='2022-05-09')
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="classes")
    hora_inicio = models.TimeField(default='09:00:00')
    hora_fim = models.TimeField(default='10:00:00')
    max_alunos = models.IntegerField(default=8)
    numero_alunos = models.IntegerField(default=0)
    class Meta:
        indexes = [models.Index(fields=["data_aula"])]
        verbose_name="agenda"
        verbose_name_plural="agendas"
        
    def __str__(self):
        return f"{self.id}: {self.data_aula} {self.hora_inicio} {self.hora_fim} {self.aula} Capacidade {self.max_alunos}"

class Usuario(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(max_length=200)
    contato = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    agendas = models.ManyToManyField(Agenda, blank=True, related_name="aulas")
    class Meta:
        indexes = [models.Index(fields=["username"])]
        verbose_name="usuario"
        verbose_name_plural="usuarios"

    def __str__(self):
        return f"{self.username}: {self.nome} {self.sobrenome} {self.agendas}"
