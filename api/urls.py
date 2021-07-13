from django.urls import path
from .views import get_atom, get_periodic_table

urlpatterns = [
    path('ptable/', get_periodic_table, name='ptable'),
    path('atom/<str:pk>/', get_atom, name='atom'),
]