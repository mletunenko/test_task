from rest_framework import serializers
from .models import Manufacturer, Dealer, CarModel, Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'engine_capacity', 'engine_power',
                  'drive_type', 'clearance', 'manufacturer']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vin', 'model', 'dealer', 'price', 'status']
