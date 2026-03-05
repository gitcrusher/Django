from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    #return HttpResponse("hello frome home")
    lucky_number = random .randint(100,999)

    vegetables = ["tomato🍅", "potato🥔", "cucumber🥒", "onion🧅", "carrot🥕"]
    person_age = 15
    context = {"lucky_number": lucky_number,"vegetables": vegetables, "person_age": person_age}
    return render(request, 'home.html', context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

def dynamic_url(request,id,name):
    print(f"the id we got for dynamic url id -> {id}")
    return render(request, 'dynamic_url.html', context = {"id":id, "name": name})