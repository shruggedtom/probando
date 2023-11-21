from django.shortcuts import render
from votar.models import Product

def index(request):
    products = Product.objects.all()
    tittle = 'Votaciones!!'
    return(render(request,"votar/index.html",{
        'tittle': tittle ,
        'products': products ,
    }))

def votar(request):
    products = Product.objects.all()
    tittle = 'Haciendo cosas!!'
    return(render(request,"votar/votar.html",{
        'tittle': tittle ,
        'x': products ,
    }))