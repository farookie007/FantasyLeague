from django.urls import path

from .views import register, UserCreateView


app_name = "accounts"

urlpatterns = [
    path("registerr/", register, name="register"),
    path("register/", UserCreateView.as_view(), name="register"),
]
