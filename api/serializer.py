from rest_framework import serializers
from .models import Atom, Particle


class AtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atom
        fields = '__all__'


class ParticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particle
        fields = '__all__'
