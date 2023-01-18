from django.contrib import admin
from .models import DistanceBasePrice,TimeMultiplierFactor,DistanceAdditionalPrice
# Register your models here.

class DistanceBasePriceAdmin(admin.ModelAdmin):
    ordering = ['price']
    

admin.site.register(DistanceBasePrice,DistanceBasePriceAdmin)
admin.site.register(DistanceAdditionalPrice)
admin.site.register(TimeMultiplierFactor)



