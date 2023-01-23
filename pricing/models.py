from django.db import models

# Create your models here.

class DistanceBasePrice(models.Model):
    price = models.FloatField()
    distance = models.FloatField()

    def __str__(self) -> str:
        return f'{self.price}/- rs Upto {self.distance}kms'

class DistanceAdditionalPrice(models.Model):
    base_fare = models.OneToOneField(DistanceBasePrice, on_delete=models.CASCADE)
    aditinal_price = models.FloatField()

    def __str__(self) -> str:
        return f'Additional {self.aditinal_price}/- rs after {self.base_fare.distance}Kms'
    
class TimeMultiplierFactor(models.Model):
    trip_time = models.FloatField()
    multiplier_value = models.FloatField()

    def __str__(self) -> str:
        return f'Under {self.trip_time} hour - {self.multiplier_value}x'


class Airline(models.Model):
    name = models.CharField(max_length=200)
    flight_no = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name} - {self.flight_no}"

class AirPorts(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.city

    


class FlightDetails(models.Model):
    flight_detail = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure = models.ForeignKey(AirPorts, on_delete=models.CASCADE,related_name = 'departure_city')
    arrival = models.ForeignKey(AirPorts, on_delete=models.CASCADE,related_name = 'arrival_city')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.flight_detail} - {self.departure} - {self.arrival} - {self.departure_time} - {self.arrival_time}'






