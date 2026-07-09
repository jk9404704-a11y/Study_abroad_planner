from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import RegisterForm, LoginForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("dashboard")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
def logout_view(request):
    auth_logout(request)
    return redirect("login")

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
