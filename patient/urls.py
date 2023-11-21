from django.urls import path
from .views import patient_dashboard, medical_history, book_appointment, patient_signup, home, aboutus, contact

urlpatterns = [
    path('', home, name="home"),
    path('aboutus/', aboutus, name="about-us"),
    path('contact/', contact, name="contact"),
    path('signup/', patient_signup, name='patient_signup'),
    path('dashboard/', patient_dashboard, name='patient_dashboard'),
    path('medical_history/', medical_history, name='medical_history'),
    path('book_appointment/', book_appointment, name= 'book_appointment'),
]