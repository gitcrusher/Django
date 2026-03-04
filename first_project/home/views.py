from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    #return HttpResponse("hello frome home")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")