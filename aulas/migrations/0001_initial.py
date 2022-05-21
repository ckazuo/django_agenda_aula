# Generated by Django 3.1.1 on 2022-05-09 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula_code', models.CharField(max_length=3)),
                ('aula_description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_aula', models.DateField(default='2022-05-09')),
                ('hora_inicio', models.TimeField(default='09:00:00')),
                ('hora_fim', models.TimeField(default='10:00:00')),
                ('max_alunos', models.IntegerField(default=8)),
                ('aula_code', models.ForeignKey(default='TESTE1', on_delete=django.db.models.deletion.CASCADE, related_name='aula', to='aulas.aulas')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=12)),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('schedule', models.ManyToManyField(blank=True, related_name='aluno', to='aulas.Schedule')),
            ],
        ),
    ]
