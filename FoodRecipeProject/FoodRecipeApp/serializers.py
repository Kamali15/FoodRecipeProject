from rest_framework import serializers
from .models import *

class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReceipe
        fields = '__all__'
    def validate_name(self, value):
        if FoodReceipe.objects.filter(name=value).exists():
            raise serializers.ValidationError("This recipe is already exists. ")
        return value
