from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Order
from .models import Contact
from .models import Customer
from .models import Profile


class customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
