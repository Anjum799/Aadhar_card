# forms.py
from django import forms
from .models import Aadhaar

class AadhaarForm(forms.ModelForm):
    class Meta:
        model = Aadhaar
        fields = ['name', 'mother_name', 'father_name', 'mobile_number', 'dob', 'gender', 'address', 'photo']   