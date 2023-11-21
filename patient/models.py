from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    surgeries = models.TextField()

    def __str__(self):
        return f"Medical History for {self.patient.user.username}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    doctor_name = models.CharField(max_length=100)
    purpose = models.TextField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient.user.username} on {self.date_time}"
