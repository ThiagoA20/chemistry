from django.shortcuts import render

def molecule(request):
    return render(request, 'dashboard.html')

def home_page(request):
    return render(request, 'home.html')
