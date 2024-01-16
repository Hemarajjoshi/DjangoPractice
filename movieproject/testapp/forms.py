from django import forms
from testapp.models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
