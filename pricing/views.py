from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DistanceBasePrice,TimeMultiplierFactor,DistanceAdditionalPrice,Airline,AirPorts,FlightDetails
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .serializer import AirPortsSerializer,FlightDetailsSerializer
import datetime

from .forms import UberRideForm


class CalculatePricing(APIView):


    def get(self, request, *args, **kwargs):
        """
        Return Price = (DBP + (D * DAP)) * TBP$ where  D → Additional distance traveled

        @GET param list to successfully perform the API:
        base_distance_travelled
        additinal_distance_travlled
        time_taken

        1) round will make base_distance_travelled to round value i.e. 4.2 -> 4 and 4.6 ->5

        """

        base_distance_travelled = self.request.query_params.get('base_distance_travelled')
        D = self.request.query_params.get('additinal_distance_travlled')
        time_taken = self.request.query_params.get('time_taken')

        if base_distance_travelled != None and  D != None and time_taken != None:
            
            DBP = DistanceBasePrice.objects.get(distance = round(float(base_distance_travelled)))
            DAP = DistanceAdditionalPrice.objects.get(base_fare=DBP)
            TBP = TimeMultiplierFactor.objects.get(trip_time=round(float(time_taken)))


            total_price = (DBP.price + (round(float(D)) * DAP.aditinal_price)) * TBP.multiplier_value

            response={
                "meta":{
                    "DBP" : DBP.price,
                    "DAP" : DAP.aditinal_price,
                    "D"   :  D,
                    "TBP" : TBP.multiplier_value
                },
                "total_price" : total_price
            }
            return Response({"status":status.HTTP_200_OK, "response":response})
        else :
            return Response(
                {
                'status':status.HTTP_400_BAD_REQUEST,
                'response': 'Please Provide base_distance_travelled, additinal_distance_travlled, time_taken param value'
                }
            )
        
class ListUsers(viewsets.ModelViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
   

    def list(self, request):
        depurture_city = self.request.query_params.get('depurture_city')
        arrival_city = self.request.query_params.get('arrival_city')
        depurture_date = self.request.query_params.get('depurture_date')

    
       

        flighs_departure_list = FlightDetails.objects.filter(departure__city = depurture_city,departure_time__date__gte=depurture_date).values_list('flight_detail', flat=True).distinct()
        flighs_arrival_list = FlightDetails.objects.filter(flight_detail__in = flighs_departure_list,arrival__city = arrival_city)
   

        ser = FlightDetailsSerializer(flighs_arrival_list,context={"depurture_city":depurture_city,'arrival_city':arrival_city},many=True)
        

        return Response({'data':ser.data})

    







        

def home_view(request):
    context = {}
    context["form"] = UberRideForm
    
    if request.method == "POST":
        formdata = UberRideForm(request.POST)
       
        
        base_distance_travelled = formdata.data["trip_distance"]
        
        # time_taken = formdata.data.end_time - formdata.data.startime 
        time_taken = 1
        D=1

        DBP = DistanceBasePrice.objects.get(distance = round(float(base_distance_travelled)))
        DAP = DistanceAdditionalPrice.objects.get(base_fare=DBP)
        TBP = TimeMultiplierFactor.objects.get(trip_time=round(float(time_taken)))

        total_price = (DBP.price + (round(float(D)) * DAP.aditinal_price)) * TBP.multiplier_value

        response={
            "meta":{
                "DBP" : DBP.price,
                "DAP" : DAP.aditinal_price,
                "TBP" : TBP.multiplier_value
            },
            "total_price" : total_price
        }
        context["total_price"] = total_price
        return render(request,'index.html',context)


    
 
    return render(request,'index.html',context)