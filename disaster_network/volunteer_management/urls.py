from django.urls import path
from . import views

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('volunteer_list',views.volunteer_list,name='volunteer_list'),
    
]
