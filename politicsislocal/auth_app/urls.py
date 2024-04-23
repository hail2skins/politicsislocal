from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

# Import the views from the website app
from . import views

urlpatterns = [
    # path to the login view
    path('login', views.login_view, name='login'),
    
    # path to the logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # path to the register view
    path('register/', views.register, name='register'),
    
    # path to built-in password reset views
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]