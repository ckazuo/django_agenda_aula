from django.contrib import admin

from .models import Aula, Agenda, Usuario

# Register your models here.
admin.site.register(Aula)
admin.site.register(Agenda)
admin.site.register(Usuario)
