from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DistanceBasePrice,TimeMultiplierFactor,DistanceAdditionalPrice
# Create your views here.


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
        
        