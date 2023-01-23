from django.urls import include, path
from .views import CalculatePricing,home_view,ListUsers
urlpatterns = [
    path('calculate-pricing/', CalculatePricing.as_view(), name=''),
    path('uber-form/', home_view, name=''),
    path('airline-check',ListUsers.as_view({'get': 'list'}))
]