from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from filme.models import film, gen
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    context = {
        'lista_filme': film.objects.all().order_by('-score')
    }
    return render(request, 'home.html', context=context)

def categorii(request):
    context = {
        'categorii': gen.objects.all().order_by('nume')
    }
    return render(request, 'categorii.html', context=context)

def categorie(request, nume):
    context = {
        'filme': film.objects.all().order_by('-score'),
        'categorie': gen.objects.get(nume=nume)
    }
    return render(request, 'categorie.html', context=context)

def film_view(request, nume):
    context = {
        'film': film.objects.get(nume=nume)
    }
    return render(request, 'film.html', context=context)

def search(request):
    if request.method == 'GET':
        cautare = request.GET['q']
        cautari = film.objects.filter(nume__icontains=cautare)|film.objects.filter(regizor__icontains=cautare)|film.objects.filter(star__icontains=cautare)
        context = {
            'nume_film': cautare,
            'cautari': cautari.order_by('nume')
        }
        return render(request, 'search.html', context=context)