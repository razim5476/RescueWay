from django.db import models
from django.utils import timezone
from user_management.models import User
# Create your models here.

    
class Disaster(models.Model):
    DISASTER_TYPES = [
        ('Earthquake', 'Earthquake'),
        ('Flood', 'Flood'),
        ('Fire', 'Fire'),
        ('Storm', 'Storm'),
    ]
    
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=100, choices=DISASTER_TYPES)
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Ongoing', 'Ongoing'), ('Resolved', 'Resolved')], default='Ongoing')

    def __str__(self):
        return self.name
    
class Report(models.Model):
     disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
     report_date = models.DateField(auto_now_add=True)
     details = models.TextField()  
     photo = models.ImageField(upload_to='disaster_reports/', blank=True, null=True)
    
    
class Alert(models.Model):
    disaster = models.ForeignKey(Disaster,on_delete=models.CASCADE)
    alert_message = models.CharField(max_length=200)
    alert_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.alert_message