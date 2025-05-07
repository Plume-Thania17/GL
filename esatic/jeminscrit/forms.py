from django import forms
from .models import Candidat

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = '__all__'
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control'}),
            'niveau_etudes': forms.Select(attrs={'class': 'form-control'}),
            'etablissement_origine': forms.TextInput(attrs={'class': 'form-control'}),
            'concours_souhaite': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'extrait_naissance': forms.FileInput(attrs={'class': 'form-control'}),
            'certificat': forms.FileInput(attrs={'class': 'form-control'}),
            'lettre_motivation': forms.FileInput(attrs={'class': 'form-control'}),
            'diplome': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }