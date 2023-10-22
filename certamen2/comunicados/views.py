from django.shortcuts import render
from .models import Comunicado, Entidad


def home(request):
    title = "Home"
    entidad_seleccionada = request.GET.get("entidad")
    
    if entidad_seleccionada == 'Todos' or entidad_seleccionada is None:
        comunicados = Comunicado.objects.all()
    else:
        entidad_a_filtrar = Entidad.objects.get(nombre=entidad_seleccionada)
        comunicados = Comunicado.objects.filter(entidad=entidad_a_filtrar)

    data = {
        "title": title,
        "total_comunicados": comunicados.count(),
        "comunicados": comunicados.order_by('-fecha_publicacion'),
        "total_entidades": Entidad.objects.count(),
        "entidades": Entidad.objects.all(),
        "entidad_seleccionada": entidad_seleccionada 
    }
    
    return render(request, 'comunicados/home.html', data)