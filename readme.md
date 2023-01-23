Install python3 venv
activate environment
clone project
cd FYR
python mange.py runserver

Navigate to admin side -> http://127.0.0.1:8000/admin
Check the API total Pricing -> http://127.0.0.1:8000/pricing/calculate-pricing/?base_distance_travelled=3&additinal_distance_travlled=2&time_taken=1

During test case judge keep the server running






Model -> Airline
flightname,code,arival date and time, arrival airport ,departure  date and time,departure airport

Airline.objects.filter(arrival_airport = "Delhi",departure_airport = "BLR", departure_date_time__gte = '24-01-2023')

* http://127.0.0.1:8000/pricing/airline-check?depurture_city=CCU&arrival_city=BLR&depurture_date=2023-01-24



{
"trip_distance" : 10,
"start_time" : 2023-01-24 14:00:00,
"end_time" : 2023-01-24 14:00:00
}

