from django.contrib import admin

from .models import Aulas, Schedule, Aluno

# Register your models here.
admin.site.register(Aulas)
admin.site.register(Schedule)
admin.site.register(Aluno)
