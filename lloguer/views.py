from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from lloguer.models import *

def autos_view(request):
    automobils = Automobil.objects.all()

    context = {
        'automobils': automobils,
    }
    
    return render(request, 'autos.html', context)