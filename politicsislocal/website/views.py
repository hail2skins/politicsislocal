from django.shortcuts import render

# import Sum to sum the values of a queryset
from django.db.models import Sum

# import the donor and contribution models from the donors app
from donors.models import Donor, Contribution

# Create your views here.
# Define the home view
def home(request):
    
    # Calculate total donors
    total_donors = Donor.objects.count() or 0
    
    # Calculate total contributed
    total_contributed = Contribution.objects.aggregate(total=Sum('amount'))['total'] or 0
    
    # Prepare a context dictionary to pass to the template
    context = {
        'total_donors': total_donors,
        'total_contributed': total_contributed
    }
    
    return render(request, "website/index.html", context)

# Define the about view
def about(request):
    return render(request, "website/about.html")

# Define the FAQ view
def faq(request):
    return render(request, "website/faq.html")
