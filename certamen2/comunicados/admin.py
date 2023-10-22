from django.contrib import admin
from .models import Comunicado, Entidad
    
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "entidad", "fecha_publicacion", "fecha_ultima_modificacion", "publicado_por", "modificado_por")
    list_filter = ("fecha_publicacion",)

    def save_model(self, request, obj, form, change):
        if not change:  # Si está creando un nuevo comunicado
            obj.publicado_por = request.user
        else: 
            obj.modificado_por = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Entidad)
admin.site.register(Comunicado, ComunicadoAdmin)

