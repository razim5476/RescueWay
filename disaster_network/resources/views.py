from django.shortcuts import render
from .models import UsefulLink, EducationalContent, EmergencyContact

def resource_list(request):
    useful_links = UsefulLink.objects.all()
    educational_content = EducationalContent.objects.all()
    emergency_contacts = EmergencyContact.objects.all()
    context = {
        'useful_links': useful_links,
        'educational_content': educational_content,
        'emergency_contacts': emergency_contacts,
    }
    return render(request, 'resources/resource_list.html', context)
