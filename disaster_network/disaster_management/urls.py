from django.urls import path
from . import views

urlpatterns = [
    path('disaster_list/',views.disaster_list,name='disaster_list'),
    path('report_disaster/',views.report_disaster,name='report_disaster'),
    path('alerts/', views.alert_list, name='alert_list'),  # New route for alert list
    path('alerts/create/', views.create_alert, name='create_alert'),  # New route for creating alerts
    path('alerts/deactivate/<int:alert_id>/', views.deactivate_alert, name='deactivate_alert'),  # Deactivate alert

]
