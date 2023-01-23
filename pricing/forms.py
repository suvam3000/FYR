from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets 

class UberRideForm(forms.Form):
    trip_distance = forms.FloatField(required=False, max_value=10, min_value=0, 
widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.01"}))
    start_time = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')
    end_time = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')

    def validate(self, value):
        
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        if self.start_time >= self.end_time :
            raise ValidationError