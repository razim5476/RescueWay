from django.db import models

# Create your models here.

class UsefulLink(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class EducationalContent(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class EmergencyContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    relationship = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} ({self.relationship})"