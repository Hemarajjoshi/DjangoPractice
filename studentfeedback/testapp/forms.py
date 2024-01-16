from django import forms

class StudentFeedback(forms.Form):
    name = forms.CharField()
    roll_no = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    

    