from django.urls import path
from .views import molecule, home_page

app_name = 'promol'

urlpatterns = [
    path('', home_page, name='home'),
    path('chemchain/', molecule, name='chemchain'),
]
