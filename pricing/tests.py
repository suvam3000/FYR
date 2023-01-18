from django.test import TestCase
from rest_framework.test import APITestCase
import requests
# Create your tests here.


class BasicTest(APITestCase):
    def test_get_totalprice_success(self):

        url = "http://127.0.0.1:8000/pricing/calculate-pricing/"

        querystring = {"base_distance_travelled":"4","additinal_distance_travlled":"2","time_taken":"2"}
        response = requests.request("GET", url,  params=querystring)
        

        self.assertEqual(response.json()['status'], 200)

    def test_get_totalprice_falure(self): # when param missing {"time_taken":"2"}

        url = "http://127.0.0.1:8000/pricing/calculate-pricing/"

        querystring = {"base_distance_travelled":"4","additinal_distance_travlled":"2"}
        response = requests.request("GET", url,  params=querystring)

        self.assertEqual(response.json()['status'], 400)