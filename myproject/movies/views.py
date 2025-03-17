from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Movie
from .forms import MovieForm
# Create your views here.

def movies_list(request):
    movies = Movie.objects.all().order_by('-date')
    return render(request, 'movies/movies_list.html', {'movies': movies})


def movies_page(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movies/movie_page.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.slug = slugify(movie.title)
            movie.save()
            return redirect('movies:list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})
