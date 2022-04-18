from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)


class Dealer(models.Model):
    name = models.CharField(max_length=50)


class Model(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    engine_capacity = models.FloatField()
    engine_power = models.FloatField()
    drive_type = models.CharField(max_length=50)
    clearance = models.IntegerField()


class Car(models.Model):
    STATUS_CHOICES = (
        ('E', 'Expected'),
        ('A', 'Available'),
        ('B', 'Booked'),
        ('S', 'Sold'),
    )
    VIN = models.CharField(max_length=17)
    model = models.ForeignKey(Model, on_delete=models.DO_NOTHING)
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
