from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm


from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView


class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:register_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'accounts/register_success.html'


class LoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
