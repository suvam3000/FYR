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
