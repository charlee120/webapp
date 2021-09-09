from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    dest1 = destination()
    dest1.name = 'Russia west'
    dest1.desc = ' nice place'
    dest1.img = 'destination_7.jpg'
    dest1.price = 900
    dest1.offer = False

    dest2 = destination()
    dest2.name = 'usa'
    dest2.desc = 'Tech place '
    dest2.img = 'destination_5.jpg'
    dest2.price = 800
    dest2.offer = False

    dest3 = destination()
    dest3.name = 'Uk'
    dest3.desc = 'nice place '
    dest3.img = 'destination_4.jpg'
    dest3.price = 300
    dest3.offer = True

    dest4 = destination()
    dest4.name = 'Russia '
    dest4.desc = 'nice place '
    dest4.img = 'destination_1.jpg'
    dest4.price = 3000
    dest4.offer = False

    dests = [dest1, dest2, dest3, dest4]

    return render(request, "index.html", {'dests':dests})