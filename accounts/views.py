from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegistrationForm


from django.views.generic.edit import FormView


class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:register_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
