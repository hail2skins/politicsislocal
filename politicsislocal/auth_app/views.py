from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .mail import send_email
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
# import settings
from django.conf import settings

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


# import django auth views to add context menu
from django.contrib.auth.views import LoginView

# Create your views here.

# Login view not technically needed but need it for the context menu
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('')
                else:
                    # Invalid password
                    form.add_error(None, "Invalid email or password")
            except User.DoesNotExist:
                # Invalid email
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()

    extra_context = {
        'title': 'Hamco IS',
        'company': 'Hamco Internet Solutions',
        'heading': 'Come in. It is cozy in here.',
        
        'form': form,
    }
    return render(request, 'registration/login.html', extra_context)

# Custom registration view
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Send a welcome email
            from_email = settings.DEFAULT_FROM_EMAIL
            from_name = settings.DEFAULT_FROM_NAME
            to_email = user.email
            subject = "Welcome to Politics is Local!"
            text_content = "Thank you for registering your account to be kept up to date as we add donors to our database."
            html_content = "<h3>Thank you for registering your account to be kept up to date as we add donors to our database.</h3>"
            send_email(from_email, from_name, to_email, subject, text_content, html_content)
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

# class PasswordResetView(auth_views.PasswordResetView):
#     template_name = 'registration/password_reset.html'
#     success_url = '/auth/password_reset/done'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'Forgot something, did we?'
#         return context

# class PasswordResetDoneView(auth_views.PasswordResetDoneView):
#     template_name = 'registration/password_reset_done.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'Check your email, even spam maybe'
#         return context

# class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
#     template_name = 'registration/password_reset_confirm.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'Fill that out. Check it twice.'
#         return context

# class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
#     template_name = 'registration/password_reset_complete.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'All done. You can login now.'
#         return context