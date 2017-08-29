from django import forms

from core.models import *


# Formulario para la clase FotoObjeto_tmp
class FotosObjetoForm(forms.ModelForm):
    class Meta:
        model = FotoObjeto_tmp
        exclude = ['objeto']
        # añadir atributos a los inputs del formulario
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            "archivo": forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# Formulario para la clase FotoSitio_tmp
class FotosSitioForm(forms.ModelForm):
    class Meta:
        model = FotoSitio_tmp
        exclude = ['sitio']
        # añadir atributos a los inputs del formulario
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            "archivo": forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }