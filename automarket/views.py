from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .serializers import ManufacturerSerializer, DealerSerializer, \
    ModelSerializer, CarSerializer
from rest_framework import status

from .models import Manufacturer, Dealer, Model, Car
from rest_framework import viewsets
from rest_framework.response import Response


class ManufacturerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Manufacturer.objects.all()
        manufacturer = get_object_or_404(queryset, pk=pk)
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = ManufacturerSerializer(data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = request.data
        serializer = ManufacturerSerializer(manufacturer, data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer.delete()
        return Response(status=status.HTTP_200_OK)


class DealerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Dealer.objects.all()
        serializer = DealerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dealer.objects.all()
        dealer = get_object_or_404(queryset, pk=pk)
        serializer = DealerSerializer(dealer)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = DealerSerializer(data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        dealer = Dealer.objects.get(pk=pk)
        data = request.data
        serializer = DealerSerializer(dealer, data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        dealer = Dealer.objects.get(pk=pk)
        dealer.delete()
        return Response(status=status.HTTP_200_OK)


class ModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Model.objects.all()
        serializer = ModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Model.objects.all()
        model = get_object_or_404(queryset, pk=pk)
        serializer = ModelSerializer(dealer)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = ModelSerializer(data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        model = Model.objects.get(pk=pk)
        data = request.data
        serializer = ModelSerializer(model, data=data, partial=True)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        model = Model.objects.get(pk=pk)
        model.delete()
        return Response(status=status.HTTP_200_OK)


class CarViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Car.objects.all()
        car = get_object_or_404(queryset, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        car = Car.objects.get(pk=pk)
        data = request.data
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_200_OK)
