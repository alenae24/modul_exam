from django.contrib import admin

from .models import Application, Review


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course_name", "desired_start_date", "payment_method", "status", "created_at")
    list_filter = ("status", "payment_method", "created_at")
    search_fields = ("course_name", "user__username", "user__full_name")
    list_per_page = 10
    readonly_fields = ("created_at", )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    search_fields = ("user__username", "user__full_name", "text")
    list_per_page = 10
