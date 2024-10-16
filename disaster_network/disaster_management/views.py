from django.shortcuts import render,redirect,get_object_or_404
from disaster_management.models import Disaster,Alert,Report
from .utils import *

# Create your views here.

def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_management/disaster_list.html', {'disasters': disasters})

def report_disaster(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        date = request.POST.get('date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        status = request.POST.get('status')
        photo = request.FILES.get('photo') 
        
        disaster = Disaster(
            name=name,
            type=type,
            date=date,
            location=location,
            description=description,
            status=status
        )      
        disaster.save()
        report = Report(
            disaster = disaster,
            details = description,  
            photo = photo,
        )
        report.save()
        
        return redirect('disaster_list')
    disaster_types = Disaster.DISASTER_TYPES
    return render(request, 'disaster_management/report_disaster.html', {'disaster_types': disaster_types})

def alert_list(request):
    alerts = Alert.objects.filter(is_active=True)
    return render(request,'disaster_management/alerts.html',{'alerts':alerts })

# disaster_management/views.py
from django.contrib import messages
from .utils import send_alert_notification

def create_alert(request):
    if request.method == 'POST':
        disaster_id = request.POST.get('disaster_id')
        alert_message = request.POST.get('alert_message')
        
        # Create the alert
        alert = Alert.objects.create(disaster_id=disaster_id, alert_message=alert_message)
        
        # Send the email notifications
        send_alert_notification(alert)
        
        messages.success(request, "Alert created and notifications sent.")
        return redirect('alert_list')
    
    disasters = Disaster.objects.all()
    return render(request, 'disaster_management/create_alert.html', {'disasters': disasters})


def deactivate_alert(request,alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    alert.is_active = False
    alert.save()
    return redirect('alert_list')