from django.urls import path
from .views import (
    RegistrationView,
    RegistrationSuccessView
)

app_name = 'accounts'

urlpatterns = [
    path('register/success/', RegistrationSuccessView.as_view(), name='register_success'),
    path('register/', RegistrationView.as_view(), name='register')
]
