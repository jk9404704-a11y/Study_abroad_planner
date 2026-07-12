from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import Country,University,Scholarship,Budget,IELTS,DocumentChecklist,Application,Timeline,Contact
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

# contact view
def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")

# login view

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")

# register view
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Registration Successful!")
        return redirect("login")

    return render(request, "register.html")
def logout_view(request):
    auth_logout(request)
    return redirect("login")

def dashboard(request):
    return render(request,'dashboard.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

# country views

def country_dashboard(request):
    countries = Country.objects.all()
    return render(request, 'country/country_list.html', {
        'countries': countries
    })

def country_details(request, id):
    country = get_object_or_404(Country, id=id)
    universities = University.objects.filter(country=country)

    return render(request, 'country/country_details.html', {
        'country': country,
        'universities': universities,
    })

# university views

def university_dashboard(request):
    universities = University.objects.all()

    return render(request, 'university/university_list.html', {
        'universities': universities
    })

# budget views
def budget_dashboard(request):
    total = None

    if request.method == "POST":
        tuition = float(request.POST.get("tuition_fee"))
        living = float(request.POST.get("living_cost"))
        other = float(request.POST.get("other_expenses"))

        total = tuition + living + other

    return render(request, "budget/budget_list.html", {
        "total": total
    })

# application views

def application_dashboard(request):

    status = None

    if request.method == "POST":
        status = request.POST.get("status")

    return render(request, "application/application_list.html", {
        "status": status
    })

# scholarship views

def scholarship_dashboard(request):
    scholarships = Scholarship.objects.all()

    return render(request, 'scholarship/scholarship_list.html', {
        'scholarships': scholarships
    })

# ielts views

def ielts_dashboard(request):
    progress = None

    if request.method == "POST":
        target = float(request.POST.get("target_score"))
        current = float(request.POST.get("current_score"))

        progress = round((current / target) * 100, 1)

        if progress > 100:
            progress = 100

    return render(request, "ielts/ielts_list.html", {
        "progress": progress
    })

# document checklist views

def document_dashboard(request):

    progress = 0

    if request.method == "POST":

        documents = [
            request.POST.get("passport"),
            request.POST.get("ielts"),
            request.POST.get("sop"),
            request.POST.get("lor"),
            request.POST.get("resume"),
            request.POST.get("offer_letter"),
            request.POST.get("visa")
        ]

        completed = sum(1 for doc in documents if doc)

        progress = round((completed / 7) * 100)

    return render(request, "documents/document_list.html", {
        "progress": progress
    })

# currency views

def currency_dashboard(request):

    converted_amount = None

    rates = {
        "USD": 1.00,
        "EUR": 0.92,
        "GBP": 0.79,
        "CAD": 1.37,
        "AUD": 1.53,
    }

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        from_currency = request.POST.get("from_currency")
        to_currency = request.POST.get("to_currency")

        usd_amount = amount / rates[from_currency]
        converted_amount = round(usd_amount * rates[to_currency], 2)

    return render(request, "currency.html", {
        "converted_amount": converted_amount
    })

# timeline views

def timeline_dashboard(request):

    if request.method == "POST":

        Timeline.objects.create(
            user=request.user,
            ielts_date=request.POST.get("ielts_date"),
            application_date=request.POST.get("application_date"),
            visa_date=request.POST.get("visa_date"),
            fly_date=request.POST.get("fly_date"),
        )

    timelines = Timeline.objects.filter(user=request.user)

    return render(request, "timeline/timeline_list.html", {
        "timelines": timelines
    })

# visa readiness views

def visa_readiness(request):
    checklist = DocumentChecklist.objects.filter(user=request.user).first()

    percentage = 0

    if checklist:
        completed = 0

        if checklist.passport:
            completed += 1
        if checklist.ielts:
            completed += 1
        if checklist.sop:
            completed += 1
        if checklist.lor:
            completed += 1
        if checklist.resume:
            completed += 1
        if checklist.offer_letter:
            completed += 1
        if checklist.visa:
            completed += 1

        percentage = round((completed / 7) * 100)

    return render(request, "visa.html", {
        "checklist": checklist,
        "percentage": percentage,
    })