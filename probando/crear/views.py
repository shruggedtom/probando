from django.shortcuts import render

def index(request):
    return(render(request,"crear/index.html"))
# Create your views here.
