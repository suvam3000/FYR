from django.urls import include, path
from .views import CalculatePricing
urlpatterns = [
    path('calculate-pricing/', CalculatePricing.as_view(), name=''),
]