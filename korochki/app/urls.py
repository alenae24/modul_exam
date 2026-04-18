from django.urls import path

from app.views import home_view, application_create_view, application_list_view, review_create_view

app_name = "app"

urlpatterns = [
    path("", home_view, name="home"),
    path("applications/create/", application_create_view, name="application_create"),
    path("applications/", application_list_view, name="application_list"),
    path("reviews/create/", review_create_view, name="review_create")
]