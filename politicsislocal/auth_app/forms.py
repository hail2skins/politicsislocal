# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import InvitationCode  # Import your InvitationCode model
from django.utils import timezone

class RegistrationForm(UserCreationForm):
    # Add email, first_name, last_name, and invitation_code fields to the UserCreationForm
    # With email and invitation_code as required
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    invitation_code = forms.CharField(max_length=36, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "invitation_code", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        # Check the invitation code
        code = self.cleaned_data["invitation_code"]
        try:
            invitation = InvitationCode.objects.get(code=code)
            if invitation.is_used:
                raise forms.ValidationError("This invitation code has already been used.")
            if invitation.expires_at and invitation.expires_at < timezone.now():
                raise forms.ValidationError("This invitation code has expired.")
            
        except InvitationCode.DoesNotExist:
            raise forms.ValidationError("Invalid invitation code.")

        if commit:
            user.save()
            invitation.is_used = True # Mark the invitation code as used
            invitation.user = user  # Set the user field of the invitation code
            invitation.save()
        
        return user
    
# Custom login form to use email instead of username
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)