from django.contrib import admin
from apps.encuesta.models import *
# Register your models here.


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dpto')

class DistritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'distrito')


admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Distrito, DistritoAdmin)
