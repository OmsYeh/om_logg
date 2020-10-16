from django import forms
from .models import Loggs


class LoggForm(forms.ModelForm):
    class Meta:
        model = Loggs
        fields = ['title', 'description']  # to use all fields of a model use __all__ in a string.

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


