from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLES = [
        ("admin", "Admin"),
        ("customer", "Customer")
    ]

    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default="Customer")

    def __str__(self):
        return self.full_name