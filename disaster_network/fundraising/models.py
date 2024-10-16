from django.db import models
from user_management.models import User

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10,decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    creation_date= models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
class Donation(models.Model):
    campaign = models.ForeignKey(Campaign,on_delete=models.CASCADE)
    donor = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.donor.full_name} - {self.campaign.title}"     
    