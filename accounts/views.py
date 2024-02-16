from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, "Account created successfully. You'll be redirected to login"
#             )
#             return redirect(reverse("user_auth:login"))
#         messages.warning(request, "Invalid parameters")
#     form = CustomUserCreationForm(request.POST)
#     return render(request, "accounts/register.html", {"form": form})


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = "user_auth:login"

    def form_valid(self, form):
        # form.save()
        messages.success(
            self.request, "Account created successfully. You'll be redirected to login."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invlalid parameters")
        return super().form_invalid(form)
