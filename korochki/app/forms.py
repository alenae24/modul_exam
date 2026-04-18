from django import forms

from app.models import Application, Review

COURSE_CHOICES = [
    ("Основы алгоритмизации и программирования", "Основы алгоритмизации и программирования"),
    ("Основы веб-дизайна", "Основы веб-дизайна"),
    ("Основы проектирования баз данных", "Основы проектирования баз данных"),
]

class ApplicationForm(forms.ModelForm):
    course_name = forms.ChoiceField(
        label="Наименование курса",
        choices=COURSE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})

    )
    desired_start_date = forms.DateField(
        label="Желаемая дата начала обучения",
        input_formats=["%d.%m.%Y"],
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ДД.ММ.ГГГГ"})
    )
    payment_method = forms.ChoiceField(
        label="Способ оплаты",
        choices=Application.PAYMENT_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Application
        fields = ("course_name", "desired_start_date", "payment_method")


class ReviewForm(forms.ModelForm):
    text = forms.CharField(
        label="Ваш отзыв",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Напишите отзыв"})
    )

    class Meta:
        model = Review
        fields = ("text",)