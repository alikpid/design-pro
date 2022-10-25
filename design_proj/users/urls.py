from django.urls import path
from .views import RegisterView, RegisterDoneView
app_name = 'users'

urlpatterns = [
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]