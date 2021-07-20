from django.db.models import manager
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AtomSerializer, ParticleSerializer
from .models import Atom, Particle


@api_view(['GET'])
def get_periodic_table(request):
    Atoms = Atom.objects.all()
    serializer = AtomSerializer(Atoms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_atom(request, pk):
    Atoms = Atom.objects.get(id=pk)
    serializer = AtomSerializer(Atoms, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_standard_model(request):
    Particles = Particle.objects.all()
    serializer = ParticleSerializer(Particles, many=True)
    return Response(serializer.data)
