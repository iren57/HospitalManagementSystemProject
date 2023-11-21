from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, MedicalHistoryForm, AppointmentForm
from .models import Patient, MedicalHistory, Appointment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'patient/home.html')


def aboutus(request):
    return render(request, 'patient/aboutus.html')


def contact(request):
    return render(request, 'patient/contact.html')
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
            return redirect('patient_dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/patient_signup.html', {'form': form})


def patient_dashboard(request):
    # # Retrieve patient data
    # patient = Patient.objects.get(user=request.user)
    #
    # # display personal details
    # return render(request, 'patient/dashboard.html', {'patient': patient})

    # Assuming you are using Django's built-in authentication system
    if request.user.is_authenticated:
        # Retrieve the Patient object associated with the logged-in user
        patient = get_object_or_404(Patient, user=request.user)
        return render(request, 'patient/dashboard.html', {'patient': patient})
    else:
        # Handle the case where the user is not authenticated
        # Redirect to login or handle it based on your requirements
        return render(request, 'patient/dashboard.html', {'patient': None})


def medical_history(request):
    # Assuming you are using Django's built-in authentication system
    if request.user.is_authenticated:
        try:
            patient = request.user.patient  # Accessing the Patient object associated with the logged-in user
            medical_history = MedicalHistory.objects.get(patient=patient)
            return render(request, 'patient/medical_history.html', {'medical_history': medical_history})
        except MedicalHistory.DoesNotExist:
            return render(request, 'patient/medical_history.html', {'medical_history': None})
    else:
        # Handle the case where the user is not authenticated
        # Redirect to login or handle it based on your requirements
        return render(request, 'patient/medical_history.html', {'medical_history': None})


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)
            appointment.save()

            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()

    return render(request, 'patient/book_appointment.html', {'form': form})
