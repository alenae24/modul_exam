from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import RegisterForm, LoginForm


# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect("app:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "customer"
            user.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect("users:login")
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("app:home")

    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Вы успешно вошли в систему")
            return redirect("app:home")
        else:
            messages.error(request, "Неверный логин или пароль")
    else:
        form = LoginForm(request)

    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect("users:login")
