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

    budget = Budget.objects.filter(user=request.user).first()

    total = 0

    if request.method == "POST":

        if budget is None:
            budget = Budget(user=request.user)

        budget.tuition_fee = request.POST.get("tuition_fee")
        budget.living_cost = request.POST.get("living_cost")
        budget.other_expenses = request.POST.get("other_expenses")

        budget.save()

    budget = Budget.objects.filter(user=request.user).first()

    if budget:
        total = budget.total_budget()

    return render(request, "budget/budget_list.html", {
        "budget": budget,
        "total": total,
    })

# application views

def application_dashboard(request):

    application = Application.objects.filter(user=request.user).first()
    universities = University.objects.all()

    if request.method == "POST":

        if application is None:
            application = Application(user=request.user)

        application.user = request.user
        application.university = University.objects.get(
            id=request.POST.get("university")
        )
        application.status = request.POST.get("status")

        application.save()

    application = Application.objects.filter(user=request.user).first()

    return render(request, "application/application_list.html", {
        "application": application,
        "universities": universities,
    })

# scholarship views

def scholarship_dashboard(request):
    scholarships = Scholarship.objects.all()

    return render(request, 'scholarship/scholarship_list.html', {
        'scholarships': scholarships
    })

# ielts views

def ielts_dashboard(request):

    ielts = IELTS.objects.filter(user=request.user).first()

    progress = 0

    if request.method == "POST":

        if ielts is None:
            ielts = IELTS(user=request.user)

        ielts.target_score = request.POST.get("target_score")
        ielts.current_score = request.POST.get("current_score")

        ielts.save()

    ielts = IELTS.objects.filter(user=request.user).first()

    if ielts:

        progress = round(
            (float(ielts.current_score) / float(ielts.target_score)) * 100,
            1
        )

        if progress > 100:
            progress = 100

    return render(request, "ielts/ielts_list.html", {
        "ielts": ielts,
        "progress": progress,
    })

# document checklist views

def document_dashboard(request):

    checklist = DocumentChecklist.objects.filter(user=request.user).first()

    if request.method == "POST":

        if checklist is None:

            checklist = DocumentChecklist(user=request.user)

        checklist.passport = bool(request.POST.get("passport"))
        checklist.ielts = bool(request.POST.get("ielts"))
        checklist.sop = bool(request.POST.get("sop"))
        checklist.lor = bool(request.POST.get("lor"))
        checklist.resume = bool(request.POST.get("resume"))
        checklist.offer_letter = bool(request.POST.get("offer_letter"))
        checklist.visa = bool(request.POST.get("visa"))

        checklist.save()

    checklist = DocumentChecklist.objects.filter(user=request.user).first()

    progress = 0

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

        progress = round((completed / 7) * 100)

    return render(request,
                  "documents/document_list.html",
                  {
                      "checklist": checklist,
                      "progress": progress,
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
        "INR": 85.50,
    
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

    timeline = Timeline.objects.filter(user=request.user).first()

    if request.method == "POST":

        if timeline is None:
            timeline = Timeline(user=request.user)

        timeline.ielts_date = request.POST.get("ielts_date")
        timeline.application_date = request.POST.get("application_date")
        timeline.visa_date = request.POST.get("visa_date")
        timeline.fly_date = request.POST.get("fly_date")

        timeline.save()

    timelines = Timeline.objects.filter(user=request.user)

    return render(request, "timeline/timeline_list.html", {
        "timeline": timeline,
        "timelines": timelines,
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