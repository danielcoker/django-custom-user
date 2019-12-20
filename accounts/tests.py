from django.test import TestCase
from django.urls import reverse
from django.test import Client

from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm, UserLoginForm

from django.db.utils import IntegrityError


User = get_user_model()


class TemplateTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Create Account', status_code=200)

    def test_signup_done(self):
        response = self.client.get(reverse('accounts:register_success'))
        self.assertTemplateUsed(response, 'accounts/register_success.html')
        self.assertContains(response, 'Registration successful', status_code=200)

    def test_signin(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Login', status_code=200)

    def test_dashboard(self):
        new_user = User.objects.create_user(
            email='johndoe@gmail.com', 
            username='johndoe', 
            password='password'
        )
        self.client.login(username='johndoe@gmail.com', password='password')

        response = self.client.get(reverse('accounts:dashboard'))
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
        self.assertContains(response, 'Welcome', status_code=200)


class TestUserModel(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='johndoe@gmail.com',
            username='johndoe',
            password='password',
            first_name='John',
            last_name='Doe'
        )
    
    def test_user_can_create_account(self):
        self.assertEquals(self.user.username, 'johndoe')

    def test_user_can_login_to_account(self):
        login_user = self.client.login(
            username='johndoe@gmail.com',
            password='password'
        )

        self.assertTrue(login_user)

    def test_users_have_unique_username(self):
        with self.assertRaises(IntegrityError) as e:
            new_user = User.objects.create_user(
            email='johndoe@gmail.com',
            username='johndoe',
            password='password',
            first_name='John',
            last_name='Doe'
        )


    def test_users_have_unique_email(self):
        with self.assertRaises(IntegrityError) as e:
            new_user = User.objects.create_user(
            email='johndoe@gmail.com',
            username='jdoe',
            password='password',
            first_name='John',
            last_name='Doe'
        )
