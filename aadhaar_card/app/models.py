# models.py
from django.db import models

class Aadhaar(models.Model):
    name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    photo = models.ImageField(upload_to='aadhaar_photos/')
    aadhaar_no = models.BigIntegerField(unique=True, null=True, blank=True)

    def str(self):
        return self.name