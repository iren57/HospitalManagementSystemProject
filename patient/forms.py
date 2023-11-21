from django import forms
from .models import Patient, MedicalHistory, Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'date_of_birth',
            'gender',
            'address',
            'phone_number',
            'emergency_contact_name',
            'emergency_contact_number',]


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = [
            'diagnosis',
            'medications',
            'allergies',
            'surgeries',]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'date_time',
            'doctor_name',
            'purpose',
        ]


