
from django.db import models
from django.contrib.auth.models import User

# country model
class Country(models.Model):
    country_name = models.CharField(max_length=100)
    flag = models.URLField(blank=True, null=True)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    living_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ielts_requirement = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.country_name
    class Meta:
        verbose_name_plural = "Countries"

# university model
class University(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=100)
    ranking = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.university_name
    class Meta:
        verbose_name_plural = "Universities"

# scholarship model
class Scholarship(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    scholarship_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    eligibility = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.scholarship_name
    
# Ielts model
class IELTS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_score = models.DecimalField(max_digits=3, decimal_places=1)
    current_score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "IELTS"
        verbose_name_plural = "IELTS"

# Budget model
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    living_cost = models.DecimalField(max_digits=10, decimal_places=2)
    other_expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def total_budget(self):
        return self.tuition_fee + self.living_cost + self.other_expenses

    def __str__(self):
        return self.user.username
    
# Documentchecklist model
class DocumentChecklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    passport = models.BooleanField(default=False)
    ielts = models.BooleanField(default=False)
    sop = models.BooleanField(default=False)
    lor = models.BooleanField(default=False)
    resume = models.BooleanField(default=False)
    offer_letter = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
# Application model
class Application(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.university.university_name}" 
    
# Timeline model
class Timeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ielts_date = models.DateField()
    application_date = models.DateField()
    visa_date = models.DateField()
    fly_date = models.DateField()

    def __str__(self):
        return self.user.username 
    
# Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    