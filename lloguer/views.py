from django.shortcuts import render
from lloguer.models import *

# Create your views here.
def inici(request):
    automoviles = Automobil.objects.all()
    # Pasar los objetos Automobil al contexto de renderizado
    return render(request, 'inicio.html', {'automoviles': automoviles})
    
