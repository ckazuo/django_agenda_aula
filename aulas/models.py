from django.db import models

# Create your models here.
class Aulas(models.Model):
    aula_code        = models.CharField(max_length=3)
    aula_description = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.aula_description} ({self.aula_code})"

class Schedule(models.Model):
    data_aula = models.DateField(default='2022-05-09')
    hora_inicio = models.TimeField(default='09:00:00')
    hora_fim = models.TimeField(default='10:00:00')
    aula_code = models.ForeignKey(Aulas, on_delete=models.CASCADE, related_name="aula", default='TESTE1')
    max_alunos = models.IntegerField(default=8)
        
    def __str__(self):
        return f"{self.aula_code}: {self.data_aula} {self.hora_inicio} {self.hora_fim} {self.aula_code} Capacidade {self.max_alunos}"

class Aluno(models.Model):
    username = models.CharField(max_length=6)
    password = models.CharField(max_length=12)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username}: {self.first} {self.last}"
