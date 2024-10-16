from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('feature/', views.feature, name='feature'),
    path('quote/', views.qoute, name='quote'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('feature/',views.feature,name='feature'),
    path('news/',views.news,name='news'),
    path('disaster/',views.disasters,name='disasters'),
    path('fund/',views.fund,name='fund'),
    path('event/',views.event,name='event'),
    path('logout/',views.logout_view,name='logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('password_reset_request',views.password_reset_request,name='password_reset_request'),
    path('otp_verification/',views.otp_verification,name='otp_verification'),
    path('set_new_password/',views.set_new_password,name='set_new_password'),
]
