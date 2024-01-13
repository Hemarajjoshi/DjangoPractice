from django import forms 

class studentRegisteration(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()