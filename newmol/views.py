from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_plot
from .utils import get_function, get_variation

def molecule(request):
    x = get_variation(-3, 3, 3000)
    y = get_function(x)
    chart = get_plot(x, y)
    return render(request, 'dashboard.html', {'chart': chart})

def home_page(request):
    return render(request, 'home.html')
