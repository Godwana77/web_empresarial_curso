from django.shortcuts import render
from .models import Store

# Create your views here.
def services(request):
    services = Store.objects.all()# Obtener todos los objetos de la tabla Service
    return render(request,'services/services.html',{'services':services})#Enviar a la plantilla el objeto services en un diccionario