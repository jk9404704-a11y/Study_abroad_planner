# My Application File
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('country_dashboard/', views.country_dashboard, name='country_dashboard'),
    path('country-details/', views.country_details, name='country_details'),
    path('university_dashboard/', views.university_dashboard, name='university_dashboard'),
    path('budget_dashboard/', views.budget_dashboard, name='budget_dashboard'),
    path('application_dashboard/', views.application_dashboard, name='application_dashboard'),
    path('scholarship-dashboard/', views.scholarship_dashboard, name='scholarship_dashboard'),
    path('ielts_dashboard/', views.ielts_dashboard, name='ielts_dashboard'),
    path('document_dashboard/', views.document_dashboard, name='document_dashboard'),
    path('currency_dashboard/', views.currency_dashboard, name='currency_dashboard'),
    path('timeline_dashboard/', views.timeline_dashboard, name='timeline_dashboard'),
    path('visa-readiness/', views.visa_readiness, name='visa_readiness'),
]
