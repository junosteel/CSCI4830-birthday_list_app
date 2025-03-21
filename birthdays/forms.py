from django import forms
from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['name', 'birth_date', 'gifts', 'priority']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }