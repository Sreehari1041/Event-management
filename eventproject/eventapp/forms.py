from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"

        widgets={
            'booking_date':DateInput(),
        }
        labels={
            'cus_name':'customer name',
            'cus_ph':'customer number',
            'name':'event name',
            'booking_date':'booking date',
            "booked_on":'booked on'


            
        }

