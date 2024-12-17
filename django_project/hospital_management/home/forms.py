from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date':DateInput()
        }

        labels = {
            'name': 'Patient Name',
            'age': 'Patient Age',
            'phone': 'Phone/Mobile',
            'email': 'Email Address',
            'doc_name': 'Select your doctor',
            'booking_date': 'Appointment Date'
        }
