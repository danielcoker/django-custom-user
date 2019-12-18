from django.urls import path
from .views import (
    RegistrationView,
    RegistrationSuccessView,
    LoginView,
    DashboardView
)

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/success/', RegistrationSuccessView.as_view(), name='register_success'),
    path('register/', RegistrationView.as_view(), name='register')
]
