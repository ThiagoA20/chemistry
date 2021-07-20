from django.urls import path
from .views import get_atom, get_periodic_table, get_standard_model

urlpatterns = [
    path('ptable/', get_periodic_table, name='ptable'),
    path('stmodel/', get_standard_model, name='stmodel'),
    path('atom/<str:pk>/', get_atom, name='atom'),
]
