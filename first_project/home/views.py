from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    #return HttpResponse("hello frome home")
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request,id):
    print(f"the id we got for dynamic url id -> {id}")
    return render(request, 'dynamic_url.html')