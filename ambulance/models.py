
from django.utils import timezone

from django.db import models

# Create your models here.
# Ambulance
# - id
# - vehicle_number
# - driver_name
# - ambulance_type
# - status (Available/Busy/Maintenance)
#
# # EmergencyRequest
# - id
# - ambulance_id -> FK
# - patient_name
# - priority (Low/Medium/High)
# - request_time -> time field
# - status (Pending/Dispatched/Completed)

class Ambulance(models.Model):
    vehicle_number=models.CharField(max_length=255,unique=True)
    driver_name=models.CharField(max_length=255)
    ambulance_type=models.CharField(max_length=255)
    ambulance_status=[
        ("Available","Available"),
        ("Busy", "Busy"),
        ("Maintenance","Maintenance")
    ]
    ambulance_status = models.CharField(max_length=20, choices=ambulance_status, default='Available')
    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.driver_name}with{self.vehicle_number}"

class Emergency_call(models.Model):
    ambulance=models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=255,null=True)
    priority_status=[
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High")
    ]
    priority_status = models.CharField(max_length=20, choices=priority_status, default='Medium')
    request_time=models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    request_status=[
        ("pending","pending"),
        ("dispatched","dispatched"),
        ("completed","completed")
    ]
    request_status = models.CharField(max_length=20, choices=request_status, default='pending')
    def __str__(self):
        return f"{self.ambulance.id}"