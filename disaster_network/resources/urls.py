from django.urls import path
from . import views


urlpatterns = [
    path('resource_list/',views.resource_list,name='resource_list'),
]
