from django.db import models
from user_management.models import User  

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    skills = models.TextField(blank=True)  
    availability = models.CharField(max_length=100)  
    phone_number = models.CharField(max_length=15)
    is_approved = models.BooleanField(default=True)
    approval_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.user.full_name

class DisasterEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class VolunteerAssignment(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    disaster_event = models.ForeignKey(DisasterEvent, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)  # Role assigned to the volunteer
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer.user.full_name} - {self.disaster_event.title}"
