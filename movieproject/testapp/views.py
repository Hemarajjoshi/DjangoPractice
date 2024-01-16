from django.shortcuts import render
from testapp.forms import MoviesForm
from testapp.models  import Movies

# Create your views here.
def home_view(request):
    return render(request, '../templates/home.html')

def add_view(request):
    form = MoviesForm
    if request.method == 'POST':
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
        return home_view(request)
    return render(request, '../templates/add.html', {'form': form})

def list_view(request):
    movies_list = Movies.objects.all()
    return render(request, '../templates/list.html', {'movies_list' : movies_list})