from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueFormAdmin(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone', 'web')

        labels = {
            'name': '',
            'address': '',
            'phone': '',
            'web': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'web': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Web Site'}),
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone')

        labels = {
            'name': '',
            'address': '',
            'phone': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        }