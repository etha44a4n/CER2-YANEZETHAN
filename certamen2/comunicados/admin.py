from django.contrib import admin
from .models import Comunicado, Entidad
from django.core.exceptions import PermissionDenied
    
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "entidad", "fecha_publicacion", "fecha_ultima_modificacion", "publicado_por", "modificado_por")
    list_filter = ("fecha_publicacion",)

    def save_model(self, request, obj, form, change):

        #Se está creando un nuevo comunicado
        if not change:
            obj.publicado_por = request.user
            if request.user.is_superuser:
                obj.entidad = None
            else:
                obj.entidad = Entidad.objects.get(nombre=str(request.user.groups.get()))

        #Se está modificando un comunicado por su creador o el admin
        elif change and (obj.publicado_por == request.user or request.user.is_superuser): 
            obj.modificado_por = request.user

        #Si se está cambiando el comunicado y el usario no pertenece al grupo con la misma entidad
        elif change and (obj.publicado_por != request.user or str(obj.entidad) != str(request.user.groups.get())):
            raise PermissionDenied("No tienes permiso para editar este comunicado.")
        super().save_model(request, obj, form, change)

admin.site.register(Entidad)
admin.site.register(Comunicado, ComunicadoAdmin)

