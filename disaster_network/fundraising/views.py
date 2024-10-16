from django.shortcuts import render,redirect,get_object_or_404
from . models import Campaign,Donation
from django.contrib.auth.decorators import login_required
from decimal import Decimal

def campaign_list(request):
    campaigns = Campaign.objects.filter(is_active=True).order_by('-creation_date')
    return render(request,'fundraising/campaign_list.html',{'campaigns':campaigns})


@login_required
def campaign(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        end_date = request.POST.get('end_date')

        # Ensure all required fields are provided
        if title and description and goal_amount and end_date:
            
            Campaign.objects.create(
                title=title,
                description=description,
                goal_amount=goal_amount,
                end_date=end_date,
                created_by=request.user,  
            )
            return redirect('campaign_list')  
        else:
            return render(request, 'fundraising/campaign.html', {
                'error_message': 'All fields are required.'
            })
    return render(request, 'fundraising/campaign.html')


@login_required
def donate_to_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign,id=campaign_id)
    
    if request.method == 'POST':
        donation_amount = request.POST.get('amount')
        
        if donation_amount:
            try:
                donation_amount = Decimal(donation_amount)
                campaign.amount_raised = donation_amount + campaign.amount_raised
                campaign.save()
                
                Donation.objects.create(
                    campaign=campaign,
                    donor=request.user,
                    amount=donation_amount
                )
                
                return redirect('campaign_list')
            except ValueError:
                return render(request,'fundraising/donations.html',{'campaign':campaign,'error_message':'Please enter a valid doantion amount'})
            
    return render(request,'fundraising/donations.html',{'campaign':campaign})

@login_required
def transaction_history(request):
    donations = Donation.objects.filter(donor=request.user).order_by('-donation_date')
    return render(request, 'fundraising/transaction_history.html', {'donations': donations})