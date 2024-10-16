from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Volunteer
from django.contrib import messages


def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request,'volunteer_management/volunteer_list.html',{'volunteers':volunteers})

@login_required
def registration(request):
    if request.method == 'POST':
        # Check if the user has already registered
        if Volunteer.objects.filter(user=request.user).exists():
            messages.warning(request, "You have already registered as a volunteer.")
            return redirect('volunteer_list')  # Redirect to the volunteer list or any desired page

        skills = request.POST.get('skills')
        availability = request.POST.get('availability')
        phone_number = request.POST.get('phone_number')
        
        # Create a new Volunteer instance
        register = Volunteer.objects.create(
            user=request.user,  # Get the logged-in user
            skills=skills,
            availability=availability,
            phone_number=phone_number
        )
        register.save()

        messages.success(request, "You have successfully registered as a volunteer.")
        return redirect('volunteer_list')  # Redirect to the volunteer list or any desired page

    return render(request, 'volunteer_management/register.html')


