from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
import re
from users.models import User


class RegistrationForm(forms.ModelForm):
    # username = forms.CharField()
    # email = forms.EmailField()
    # phone = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'password',
        ]

        widgets = {
            'password': forms.PasswordInput(),
        }

        help_texts = {
            'username': None,
        }

        labels = {
            'username': 'Имя пользователя',
        }

    def save(self, commit=True):
        self.instance.password = make_password(
            self.cleaned_data['password']
        )
        return super().save(self)

    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        else:
            return self.cleaned_data

    def clean_username(self):
        username = self.data['username']
        if not re.match("^[A-Za-z0-9_]*$", username):
            raise forms.ValidationError("Имя пользователя может содержать только буквы и цифры")

        return username

    def clean_phone(self):
        phone = self.data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone should contain only digits")

        return phone


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def get_user(self, request):
        return authenticate(
            request,
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
