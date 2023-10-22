from django.contrib import admin
from .models import Comunicado, Entidad

class comunicados(admin.ModelAdmin):
    list_display=("titulo","tipo","entidad","fecha_publicacion","fecha_ultima_modificacion", "publicado_por")
    list_filter=("fecha_publicacion",)

admin.site.register(Entidad)
admin.site.register(Comunicado, comunicados)
