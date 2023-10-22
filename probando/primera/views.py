from django.shortcuts import render

def index(request):
    return(render(request,'primera/index.html'))
# Create your views here.
