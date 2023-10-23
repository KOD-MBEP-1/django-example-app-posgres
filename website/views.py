from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Movie

# Create your views here.
def index (request):
    try:
        movies = Movie.objects.all()
        return render(request, 'index.html', context={
            'movies' : movies,
        })
    except Movie.DoesNotExist:
        return HttpResponse('No movies in the database')