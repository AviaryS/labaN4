from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Films, Category
from .forms import FilmForm


def index(request):
    films = Films.objects.all()
    return render(request, 'engine/index.html', {'films': films})


def add(request):
    form = FilmForm()
    create_categories()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'engine/add.html', {'form': form})


def edit(request, id):
    try:
        film = Films.objects.get(id=id)
        if request.method == 'POST':
            form = FilmForm(request.POST, instance=film)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = FilmForm()
            return render(request, 'engine/edit.html', {'form': form})
    except:
        return HttpResponseNotFound('<h2>Film not found</h2>')


def delete(request, id):
    try:
        film = Films.objects.get(id=id)
        film.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound('<h2>Film not found</h2>')


def create_categories():
    if Category.objects.count() == 0:
        Category.objects.create(name='Роман')
        Category.objects.create(name='Ужасы')
        Category.objects.create(name='Комедия')