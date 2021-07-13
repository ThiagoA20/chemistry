from django.urls import path
from .views import molecule, home_page

app_name = 'promol'

urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', molecule, name='dashboard'),
]
