from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from .forms import LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Login successful")
                return redirect(reverse("leagues:league_create"))
            messages.error(request, "Invalid matric number or password")
        else:
            messages.error(request, "Invalid form submission")
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, "user_auth/login.html", {"form": form})


# class UserLoginView(LoginView):
#     template_name = "user_auth/login.html"
#     form_class = LoginForm
#     success_url = reverse_lazy("leagues:league_create")
#     redirect_authenticated_user = True

#     def form_invalid(self, form):
#         messages.error(self.request,'Invalid username or password')
#         return self.render_to_response(self.get_context_data(form=form))
