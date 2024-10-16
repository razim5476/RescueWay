from django.urls import path
from . import views

urlpatterns = [
    path('campaign/',views.campaign,name='campaign'),
    path('campaign/<int:campaign_id>/donate/', views.donate_to_campaign, name='donate_to_campaign'),
    path('campaign_list/',views.campaign_list, name='campaign_list'),
    path('transaction_history/', views.transaction_history, name='transaction_history'),
    

]
