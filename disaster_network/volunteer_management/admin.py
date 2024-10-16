from django.contrib import admin
from . models import Volunteer
from django.utils import timezone
# Register your models here.

@admin.register(Volunteer)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved','approval_date')
    list_filter = ('is_approved',)
    actions = ['approve_volunteer']
    
    def approve_volunteer(self,request,queryset):
        queryset.update(is_approved=True,approval_date=timezone.now())
        self.message_user(request,"Selected volunteers have been approved.")
    approve_volunteer.short_description = "Approve selected volunteers"
    
