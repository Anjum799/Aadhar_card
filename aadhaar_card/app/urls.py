# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.aadhaar_form, name='aadhaar_form'),
    path('full_card/<int:aadhaar_id>/', views.aadhaar_full_card, name='aadhaar_full_card'),
    path('short_card/<int:aadhaar_id>/', views.aadhaar_short_card, name='aadhaar_short_card'),
]