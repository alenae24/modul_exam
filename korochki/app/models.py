from django.conf import settings
from django.db import models


# Create your models here.
class Application(models.Model):
    PAYMENT_CHOICES = [
        ("cash", "Наличными"),
        ("phone", "Перевод по номеру телефона"),
    ]

    STATUS_CHOICES = [
        ("new", "Новая"),
        ("in_progress", "Идет обучение"),
        ("completed", "Обучение завершено"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="application",
        verbose_name="Пользователь"
    )
    course_name = models.CharField("Наименование курса", max_length=255)
    desired_start_date = models.DateField("Желаемая дата начала обучения")
    payment_method = models.CharField("Способ оплаты", max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.course_name} - {self.user.username}"

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Пользователь"
    )
    text = models.TextField("Текст отзыва")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв {self.user.username}"
