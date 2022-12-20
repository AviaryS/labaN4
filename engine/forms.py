from django import forms
from engine.models import Films


class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = '__all__'