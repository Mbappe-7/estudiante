
from django.contrib import admin
from .models import Programa, Materia, Estudiante


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "estado")  # mostrar estas columnas en la tabla
    list_filter = ("estado",)  # filtros en el lateral
    search_fields = ("nombre",)


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "profesor", "programa")
    list_filter = ("programa",)
    search_fields = ("nombre", "profesor")


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad")
    search_fields = ("nombre",)
    filter_horizontal = ("materias",)  # mejor selector para ManyToMany