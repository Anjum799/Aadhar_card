# views.py
import random
from django.shortcuts import render, redirect
from .models import Aadhaar
from .forms import AadhaarForm

def aadhaar_form(request):
    if request.method == "POST":
        form = AadhaarForm(request.POST, request.FILES)
        if form.is_valid(): 
            aadhaar = form.save(commit=False)
            aadhaar.aadhaar_no = random.randint(100000000000,999999999999)  # Generate Aadhaar No
            aadhaar.save()
            return redirect('aadhaar_full_card', aadhaar_id=aadhaar.id)
    else:
        form = AadhaarForm()
    return render(request, 'aadhaar_form.html', {'form': form})

def aadhaar_full_card(request, aadhaar_id):
    try:
        aadhaar = Aadhaar.objects.get(id=aadhaar_id)
    except Aadhaar.DoesNotExist:
        aadhaar = None  # Handle the case where Aadhaar doesn't exist

    return render(request, 'aadhaar_full_card.html', {'aadhaar': aadhaar})

def aadhaar_short_card(request, aadhaar_id):
    try:
        aadhaar = Aadhaar.objects.get(id=aadhaar_id)
    except Aadhaar.DoesNotExist:
        aadhaar = None

    return render(request, 'aadhaar_short_card.html', {'aadhaar':aadhaar})