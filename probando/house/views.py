from django.shortcuts import render
from house.models import Product

def index(request):
    products = Product.objects.all()
    tittle = 'Haciendo cosas!!'
    return(render(request,"house/index.html",{
        'tittle': tittle ,
        'products': products ,
    }))
