from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import ApplicationForm, ReviewForm
from app.models import Application


def home_view(request):
    return render(request, "app/home.html")


@login_required
def application_create_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.status = "new"
            application.save()
            messages.success(request, "Заявка успешно отправлена")
            return redirect("app:application_list")
    else:
        form = ApplicationForm()

    return render(request, "app/application_form.html", {"form": form})


@login_required
def application_list_view(request):
    applications = Application.objects.filter(user=request.user).order_by("-created_at")
    can_review = applications.filter(status="completed").exists()

    return render(request, "app/application_list.html", {
        "applications": applications,
        "can_review": can_review
    })


@login_required
def review_create_view(request):
    has_completed = Application.objects.filter(user=request.user, status="completed").exists()

    if not has_completed:
        messages.error(request, "Оставить отзыв можно только после завершения обучения")
        return redirect("app:application_list")

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Спасибо! Ваш отзыв добавлен")
            return redirect("app:application_list")
    else:
        form = ReviewForm()

    return render(request, "app/review_form.html", {"form": form})