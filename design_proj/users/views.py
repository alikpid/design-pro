from .forms import RegisterUserForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'register_done.html'
