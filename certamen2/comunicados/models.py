from django.db import models
from django.contrib.auth.models import User

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    logo = models.ImageField()
    usuario_admin = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

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
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, editable=False, null=True)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)
    modificado_por = models.ForeignKey(User, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)
    
    def __str__(self) -> str:
        return self.titulo
