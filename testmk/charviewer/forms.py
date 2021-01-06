from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
from django import forms
from charviewer.models import Notes

# class LoginForm(forms.Form):
#     # username = forms.CharField(label='username', max_length=100)
#     email = forms.EmailField(label='email', max_length=100)
#     password = forms.CharField(label='password', widget=forms.PasswordInput)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes

        fields = [
            'note',
            'move_id',
        ]

    # def check_note_exists(self):
    #     note = self.cleaned_data.get('move_id')
    #     if Notes.objects.filter(move_id=note).exists():
    #         raise forms.ValidationError(
    #             'This note already exists.')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email address is already in use.')
        else:
            return self.cleaned_data['email']

