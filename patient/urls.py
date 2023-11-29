from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import patient_dashboard ,patient_signup, home
from .import views

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', patient_signup, name='patient_signup'),
    path('dashboard/', patient_dashboard, name='patient_dashboard'),

    path('medical_history/', views.homeMedical, name='medical_history'),
    path('insert', views.insertMedical, name='insertData'),
    path('update/<int:id>', views.updateMedical, name='updateData'),
    path('delete/<int:id>', views.deleteMedical, name='deleteData'),

    path('appointment_list/', views.homeAppointment, name= 'appointment_list'),
    path('insertAppointment', views.InsertAppointment, name='insertAppointment'),
    path('edit_appointment/<id>/', views.edit_appointment, name='edit_appointment'),
    path('delete_appointment/<id>/', views.delete_appointment, name='delete_appointment'),

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]