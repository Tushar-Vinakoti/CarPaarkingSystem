from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('2W', 'Two Wheeler'),
        ('4W', 'Four Wheeler'),
        ('HV', 'Heavy Vehicle'),
        ('OT', 'Other')
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=15, default='')
    vehicle_number = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=50, default='')
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPES, default='OT')
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner_name} - {self.vehicle_number}"

    class Meta:
        ordering = ['-created_at']