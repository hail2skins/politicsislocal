from django.urls import path

from . import views

urlpatterns = [
    # Add a URL pattern for the donor_list view
    path('list', views.donor_list, name='list'),

]
    