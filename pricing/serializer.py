from rest_framework import serializers
from .models import Airline,AirPorts,FlightDetails

class AirlineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Airline
        fields = '__all__'

class AirPortsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AirPorts
        fields = '__all__'

class FlightDetailsSerializer(serializers.Serializer):
    
    flight_detail = serializers.SerializerMethodField()
    connectings = serializers.SerializerMethodField()
    departure_time =  serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    arrival_time =  serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FlightDetails
        fields = ['id','flight_detail','connectings','departure_time','arrival_time']

    def get_flight_detail(self, obj):
        obj2 = Airline.objects.get(id=obj.flight_detail.id)
        
        return {"name" : obj2.name, "flight_no" : obj2.flight_no}

    

    def get_connectings(self,obj):
        final_out = self.context["depurture_city"]
        air_detail = Airline.objects.get(id=obj.flight_detail.id)
        departure_point = FlightDetails.objects.get(departure__city = self.context["depurture_city"],flight_detail = air_detail)
        
        recursive_departure = departure_point.arrival.city

        if recursive_departure == self.context["arrival_city"] :
            return final_out + ' - ' + recursive_departure + f"({departure_point.arrival_time})"

        final_out = final_out + ' - ' + recursive_departure + f"({departure_point.arrival_time})"
        while recursive_departure != self.context["arrival_city"] :
            
            departure_point = FlightDetails.objects.get(departure__city = recursive_departure,flight_detail = air_detail)
            recursive_departure = departure_point.arrival.city
            final_out = final_out + ' - ' + recursive_departure + f"({departure_point.arrival_time})"
            
        
        return final_out

class UberSerializer(serializers.Serializer):
    
    trip_distance = serializers.IntegerField(
        style={'placeholder': 'Email', 'autofocus': True}
    )
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
