from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    #return HttpResponse("hello frome home")
    lucky_number = random .randint(100,999)

    vegetables = ["tomato🍅", "potato🥔", "cucumber🥒", "onion🧅", "carrot🥕"]
    person_age = 15
    cities  = [
        {"Name": "New York", "Population": 8000000, "Country": "USA"},
        {"Name": "Tokyo", "Population": 14000000, "Country": "Japan"},
        {"Name": "Paris", "Population": 2000000, "Country": "France"},
        {"Name": "London", "Population": 9000000, "Country": "UK"}
    ]

    context = {"lucky_number": lucky_number,"vegetables": vegetables, "person_age": person_age, "cities": cities}
    return render(request, 'home.html', context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request,id,name):
    print(f"the id we got for dynamic url id -> {id}")
    return render(request, 'dynamic_url.html', context = {"id":id, "name": name})

def project(request):
    lucky_number = random .randint(0,99)
    context = {"lucky_number": lucky_number}
    return render(request, 'project/project.html',context)