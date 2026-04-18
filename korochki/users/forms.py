import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите логин"})
    )

    full_name = forms.CharField(
        label="ФИО",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите ФИО"})
    )

    phone = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "8(999)000-00-00"})
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите электронную почту"})
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Минимум 8 символов"})
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Повторите пароль"})
    )

    class Meta:
        model = User
        fields = ("username", "full_name", "phone", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ""

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.fullmatch(r"[A-Za-z0-9]{6,}", username):
            raise forms.ValidationError("Логин должен содержать только латиницу и цифры, минимум 6 символов")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой логин уже существует")
        return username

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if not re.fullmatch(r"[А-Яа-яЁё\s]+", full_name):
            raise forms.ValidationError("ФИО должно содержать только кириллицу и пробелы")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not re.fullmatch(r"8\(\d{3}\)\d{3}-\d{2}-\d{2}", phone):
            raise forms.ValidationError("Телефон должен быть в формате 8(ХХХ)ХХХ-ХХ-ХХ")
        return phone

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже используется")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите логин"})
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Введите пароль"})
    )