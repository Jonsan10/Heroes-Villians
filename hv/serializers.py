from rest_framework import serializers
from .models import HV

class HVSerializer(serializers.ModelSerializer):
    class Meta:
        model = HV
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase']