from django.db import models

# Create your models here.

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField()

    def __str__(self) -> str:
        return self.nombre


class Comunicado(models.Model):
    TIPO_CHOICES = [
        ("S", "Suspensión de actividades"),
        ("C", "Suspención de clase"),
        ("I", "Información"),
    ]

    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    detalle = models.TextField()
    detalle_corto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo


