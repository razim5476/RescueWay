from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login as lg,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.core.mail import send_mail
from datetime import datetime
from blog_app.models import *

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user_posts = BlogPost.objects.filter(author=request.user)
    else:
        user_posts = BlogPost.objects.none()
    return render(request,'index.html',{'posts': user_posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def detail(request):
    return render(request,'detail.html')

def feature(request):
    return render(request,'feature.html')

def qoute(request):
    return render(request,'qoute.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def features(request):
    return render(request,'feature.html')

def news(request):
    return render(request,'news.html')

def disasters(request):
    return render(request,'disasters.html')

def fund(request):
    return render(request,'fund.html')

def event(request):
    return render(request,'events.html')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        errors = {}
        
        if password != confirm_password:
            errors['password_mismatch'] = 'Password do not match'
        
        if User.objects.filter(email=email).exists():
            errors['email_taken'] = 'email already taken'
            
        if not errors:
            user = User(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                password=make_password(password)  
            )
            user.save()
            return redirect('login')
        
        return render('signup.html',{errors:'errors'})
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            lg(request, user)
            return render(request,'index.html')
        else:
            errors = 'invalid password or email'
            return render('login.html',{'errors':errors})
     
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def user_profile(request):
    if request.method == "POST":
        user = request.user
        user.full_name = request.POST.get('username')  
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone')
        user.bio = request.POST.get('bio')

        dob_str = request.POST.get('dob')  # Get the date of birth as a string
        if dob_str:  # Ensure dob_str is not empty
            try:
                user.dob = datetime.strptime(dob_str, "%Y-%m-%d").date()  # Convert to date
            except ValueError:
                messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
                return redirect('user_profile')

        if request.FILES.get('image'):
            user.image = request.FILES['image']
        
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('user_profile')

    return render(request, 'user_profile.html', {'user': request.user})


#password reset views
#generate otp
#password_reset_request
#opt_verification
#new_password_set

def generate_otp():
    return random.randint(100000,999999)

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['user_email'] = email
            
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                'rescueway73@gmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('otp_verification')
        except User.DoesNotExist:
            return render(request,'password_reset_request.html',{'error':'Email not registered'})
            
    return render(request,'password_reset_request.html')

def otp_verification(request):
    if request.method == 'POST':
        entered_otp = request.POST['otp']
        if str(entered_otp) == str(request.session.get('otp')):
            return redirect('set_new_password')
        else:
            return render(request, 'otp_verification.html', {'error': 'Invalid OTP.'})

    return render(request, 'otp_verification.html')

def set_new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')  # Use .get() for safer access
        email = request.session.get('user_email')  # Ensure you're using the correct session key
        
        if email:  # Check if email is found in the session
            try:
                user = User.objects.get(email=email)  # Retrieve user by email
                user.set_password(new_password)  # Set the new password
                user.save()  # Save the user
                messages.success(request, 'Password has been reset successfully.')  # Success message
                return redirect('login')  # Redirect to login page
            except User.DoesNotExist:
                messages.error(request, 'User not found. Please try again.')  # User not found error
                return render(request, 'set_new_password.html')  # Render the same page
        else:
            messages.error(request, 'No email found in session. Please request a password reset again.')  
            return render(request, 'set_new_password.html') 
            
    return render(request, 'set_new_password.html') 
    
        
    