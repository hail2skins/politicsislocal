from django.urls import path

# Import the views from the website app
from . import views

urlpatterns = [
        
    # Path to the home view
    path("", views.home, name=""),
    
]