from django.shortcuts import render
from . import forms

# Create your views here.
def feedback_view(request):
    form = forms.StudentFeedback()
    if request.method == 'POST':
        form = forms.StudentFeedback(request.POST)
        if form.is_valid():
            print("Form validation successful")
            print('Student Name: ', form.cleaned_data['name'])
            print("Roll no:", form.cleaned_data['roll_no'])
            print('Email:' , form.cleaned_data['email'])
            print('feedback: ', form.cleaned_data["feedback"])

    return render(request, '../templates/feedback.html', {'form' : form})
