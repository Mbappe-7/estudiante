from django.db import models


class Programa(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
        ("EN_REVISION", "En revisión"),
        ("CERRADO", "Cerrado"),
    ]
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default="ACTIVO")

    def _str_(self): 
        return f"{self.nombre} ({self.estado})"


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="materias"
    )

    def _str_(self): 
        return f"{self.nombre} ({self.programa.nombre})"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    materias = models.ManyToManyField(Materia, related_name="estudiantes")

    def _str_(self): 
        return self.nombre