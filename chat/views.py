from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


def main_page(request):
    return render(request, 'chat/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'chat/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'chat/login.html'



def logout_user(request):
    logout(request)
    return redirect('login')