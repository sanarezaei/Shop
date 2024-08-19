from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    reverse_lazy = reverse_lazy('login')
    