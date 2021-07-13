from rest_framework import serializers
from .models import Atom


class AtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atom
        fields = '__all__'
