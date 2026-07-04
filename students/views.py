from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def dashboard(request):
    return render(request,'dashboard.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def country_dashboard(request):
    return render(request,'country.html')

def country_details(request):
    return render(request,'country_details.html')

def university_dashboard(request):
    return render(request,'universities.html')

def budget_dashboard(request):
    return render(request,'budget.html')

def application_dashboard(request):
    return render(request,'application.html')

def scholarship_dashboard(request):
    return render(request,'scholarships.html')

def ielts_dashboard(request):
    return render(request, 'ielts.html')

def document_dashboard(request):
    return render(request, 'documents.html')

def currency_dashboard(request):
    return render(request, 'currency.html')

def timeline_dashboard(request):
    return render(request, 'timeline.html')

def visa_readiness(request):
    return render(request, 'visa.html')
