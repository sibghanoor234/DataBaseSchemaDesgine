import past
from django.utils import timezone
from django.contrib.auth import password_validation
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    consultation_fees = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr {self.name}"

class Patient(models.Model):
    name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='M')
    dob = models.DateField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient {self.name}"

class Labtests(models.Model):
        test_name = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        discription = models.TextField(max_length=255, null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return f"test_name{self.test_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    remarks = models.TextField(null=True, blank=True)
    lab_tests = models.ManyToManyField(Labtests, blank=True)
    APPOINTMENT_STATUS_CHOICES = [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=255, choices=APPOINTMENT_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment {self.patient.name} with {self.doctor.name}  at {self.date_time}"


class Medicine(models.Model):
    medicine_name= models.CharField(max_length=255)
    strength=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    stock=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"medicine{self.medicine_name} with{self.price} at {self.stock}"

class Bill(models.Model):
    appointment  = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor_fee=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    lab_total=models.DecimalField(max_digits=5,decimal_places=2,default=0)
    medicine_total=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    discount=models.DecimalField(max_digits=5,decimal_places=1,default=0)
    tax=models.DecimalField(max_digits=4,decimal_places=1,default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    payment_status=  [
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
    ]
    payment_date=models.DateTimeField(default=timezone.now)
    payment_method=  [
        ("Cash", "Cash"),
        ("Card", "Card"),
    ]
    payment_status = models.CharField(max_length=20,choices=payment_status,default='Pending')
    payment_method = models.CharField(max_length=20, choices=payment_method,  default='Cash')
    def grand_total(self):
        return (
            self.doctor_fee
            + self.medicine_total
            + self.lab_total
            - self.discount
            +self.tax
        )
    def __str__(self):
        return f"{self.appointment.id}"














