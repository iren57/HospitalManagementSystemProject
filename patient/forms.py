from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Patient, MedicalHistory, Appointment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'date_of_birth',
            'gender',
            'address',
            'phone_number',
            'emergency_contact_name',
            'emergency_contact_number', ]


# class MedicalHistoryForm(forms.ModelForm):
#     class Meta:
#         model = MedicalHistory
#         fields = [
#             'diagnosis',
#             'medications',
#             'allergies',
#             'surgeries', ]


# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = [
#             'date_time',
#             'doctor_name',
#             'purpose',
#         ]
#         widgets = {
#             'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
