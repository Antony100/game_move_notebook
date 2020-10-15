from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password', 'password2']

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

    # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')




# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password',
#                                widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password',
#                                 widget=forms.PasswordInput)
#     email = forms.EmailField(
#         max_length=255, help_text='Enter a valid email address')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name','last_name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']

#     def clean_email(self):
#         # Get the email
#         email = self.cleaned_data.get('email')

#         # Check to see if any users already exist with this email as a username.
#         try:
#             match = User.objects.get(email=email)
#         except User.DoesNotExist:
#             # Unable to find a user, this is fine
#             return email

#     # A user was found with this as a username, raise an error.
#         raise forms.ValidationError('This email address is already in use.')


