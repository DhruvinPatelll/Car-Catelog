from rest_framework import serializers
from .models import CarCategory, CarList

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = '__all__'
        
class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = '__all__'