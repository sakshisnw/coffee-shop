from django.shortcuts import render, get_object_or_404
from .models import Coffee

# Create your views here.
def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'menu/coffee_list.html', {'coffees': coffees})

def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'menu/coffee_detail.html', {'coffee': coffee})

