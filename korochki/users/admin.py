from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["username", "full_name", "phone", "email", "role"]

    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {
            "fields": ("full_name", "phone", "role")
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {
            "fields": ("full_name", "phone", "email", "role")
        }),
    )
