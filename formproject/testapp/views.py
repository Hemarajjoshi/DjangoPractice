from django.shortcuts import render
from . import forms
# Create your views here.

def studentregisterview(request):
    form = forms.studentRegisteration()
    return render(request, '../templates/home.html', {'form': form})
