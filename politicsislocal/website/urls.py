from django.urls import path

# Import the views from the website app
from . import views

urlpatterns = [
        
    # Path to the home view
    path("", views.home, name=""),
    
    # Path to the about view
    path("about", views.about, name="about"),
    
    # Path to the FAQ view
    path("faq", views.faq, name="faq"),
    
]