from rest_framework import serializers
from .models import Manufacturer, Dealer, Model, Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name', 'engine_capacity', 'engine_power',
                  'drive_type', 'clearance', 'manufacturer']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'VIN', 'model', 'dealer', 'price', 'status']
