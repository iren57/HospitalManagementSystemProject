from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient, MedicalHistory, Appointment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse


def home(request):
    return render(request, 'patient/index.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


@login_required
def patient_dashboard(request):
    # Assuming you are using Django's built-in authentication system
    patient = request.user.patient  # Assuming you have a OneToOneField between User and Patient
    return render(request, 'patient/dashboard.html', {'patient': patient})


def patient_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Patient instance for the user
            patient = Patient.objects.create(user=user)

            # Log in the user
            login(request, user)

            # Redirect to the patient dashboard
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'patient/patient_signup.html', {'form': form})


def patient_dashboard(request):
    # Retrieve patient data
    patient = Patient.objects.get(user=request.user)

    # display personal details
    return render(request, 'patient/dashboard.html', {'patient': patient})

    # Assuming you are using Django's built-in authentication system
    # if request.user.is_authenticated:
    #     # Retrieve the Patient object associated with the logged-in user
    #     patient = get_object_or_404(Patient, user=request.user)
    #     return render(request, 'patient/base.html', {'patient': patient})
    # else:
    #     # Handle the case where the user is not authenticated
    #     # Redirect to login or handle it based on your requirements
    #     return render(request, 'patient/base.html', {'patient': None})


def homeMedical(request):  # READ DATA

    user = request.user
    patient = Patient.objects.get(user=user)

    data = MedicalHistory.objects.filter(patient__user=request.user)
    return render(request, 'patient/medical_history.html', {'data': data})


def insertMedical(request):  # CREATE DATA
    # Get user-specific information
    user = request.user
    patient = Patient.objects.get(user=user)

    if request.method == 'POST':
        diagnosis = request.POST.get("diagnosis")
        medications = request.POST.get("medications")
        allergies = request.POST.get("allergies")
        surgeries = request.POST.get("surgeries")

        # Get the current user's patient instance
        patient = Patient.objects.get(user=request.user)

        # Create a new MedicalHistory instance associated with the patient
        query = MedicalHistory(patient=patient, diagnosis=diagnosis, medications=medications, allergies=allergies,
                               surgeries=surgeries)
        query.save()
        return redirect(reverse('medical_history'))
    else:
        return redirect(request, 'patient/medical_history.html')


def updateMedical(request, id):  # UPDATE DATA
    if request.method == 'POST':
        diagnosis = request.POST.get("diagnosis")
        medications = request.POST.get("medications")
        allergies = request.POST.get("allergies")
        surgeries = request.POST.get("surgeries")

        edit = MedicalHistory.objects.get(id=id)
        edit.diagnosis = diagnosis
        edit.medications = medications
        edit.allergies = allergies
        edit.surgeries = surgeries
        edit.save()
        return redirect(reverse('medical_history'))
    else:
        d = MedicalHistory.objects.get(id=id)
        return render(request, 'patient/editMedical_history.html', {'d': d})


def deleteMedical(request, id):
    d = MedicalHistory.objects.get(id=id)
    d.delete()
    return redirect(reverse('medical_history'))


def InsertAppointment(request):  # CREATE DATA

    user = request.user
    patient = Patient.objects.get(user=user)

    if request.method == 'POST':
        date_time = request.POST.get("date_time")
        doctor_name = request.POST.get("doctor_name")
        purpose = request.POST.get("purpose")

        # Get the current user's patient instance
        patient = Patient.objects.get(user=request.user)

        # Create a new MedicalHistory instance associated with the patient
        query = Appointment(patient=patient, date_time=date_time, doctor_name=doctor_name, purpose=purpose)
        query.save()
        return redirect(reverse('appointment_list'))
    else:
        return redirect(request, 'patient/book_appointment.html')



def homeAppointment(request):  # READ DATA

    user = request.user
    patient = Patient.objects.get(user=user)

    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'patient/book_appointment.html', {'appointments': appointments})


def edit_appointment(request, id):  # UPDATE DATA
    if request.method == 'POST':
        date_time = request.POST.get("date_time")
        doctor_name = request.POST.get("doctor_name")
        purpose = request.POST.get("purpose")

        edit = Appointment.objects.get(id=id)
        edit.date_time = date_time
        edit.doctor_name = doctor_name
        edit.purpose = purpose
        edit.save()
        return redirect('appointment_list')
    else:
        appointment = Appointment.objects.get(id=id)
    return render(request, 'patient/edit_appointment.html', { 'appointment': appointment})


def delete_appointment(request, id):  # DELETE DATA
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return redirect('appointment_list')

# def book_appointment(request):
#     patient = Patient.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = Patient.objects.get(user=request.user)
#             appointment.save()
#
#             return redirect('patient_dashboard')
#     else:
#         form = AppointmentForm()
#
#         # Retrieve and display appointments for the current patient
#         appointments = Appointment.objects.filter(patient=patient)
#
#     return render(request, 'patient/book_appointment.html', {'form': form})
