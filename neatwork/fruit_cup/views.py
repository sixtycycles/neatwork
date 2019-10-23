from django.shortcuts import render
from .models import Building

# Create your views here.

def home_page (request):

    all_buildings = Building.objects.all()

    data = {'all_buildings': all_buildings}
    return render (request, 'fruit_cup/home_page.html', data)