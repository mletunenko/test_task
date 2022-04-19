from .serializers import ManufacturerSerializer, DealerSerializer, \
    CarModelSerializer, CarSerializer
from rest_framework import status
from rest_framework.decorators import action
from .models import Manufacturer, Dealer, CarModel, Car
from rest_framework import viewsets
from rest_framework.response import Response


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=True, methods=['put'])
    def sell_car(self, request, pk=None):
        car = Car.objects.filter(pk=pk).first()
        if car and car.status == Car.STATUS_AVAILABLE:
            car.status = Car.STATUS_SOLD
            car.save()
            serializer = CarSerializer(car)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {
                'response': 'The Car is not available for sale'
            }
            return Response(data)
