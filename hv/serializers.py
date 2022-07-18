from rest_framework import serializer
from .models import HV

class HVSerializer(serializer.ModelSerializer):
    class Meta:
        model = HV
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase']