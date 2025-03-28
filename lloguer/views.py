from django.shortcuts import render, redirect
from django import forms
from lloguer.models import Automobil, Reserva
from django.contrib.auth.models import User
from django.utils import timezone

# Crear el formulario directamente en views.py
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['automobil', 'usuari', 'data_inici', 'data_final']

    def clean(self):
        cleaned_data = super().clean()
        automobil = cleaned_data.get('automobil')
        data_inici = cleaned_data.get('data_inici')

        if Reserva.objects.filter(automobil=automobil, data_inici=data_inici).exists():
            raise forms.ValidationError("Ya existe una reserva para este automóvil en esta fecha.")
        
        return cleaned_data

def reserva_view(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autos')  # Redirigir a la página de autos después de guardar
    else:
        form = ReservaForm()

    context = {
        'form': form,
        'automobils': Automobil.objects.all(),  # Mostrar los automóviles disponibles
    }
    return render(request, 'reserva.html', context)

def autos_view(request):
    automobils = Automobil.objects.all()

    context = {
        'automobils': automobils,
    }
    
    return render(request, 'autos.html', context)