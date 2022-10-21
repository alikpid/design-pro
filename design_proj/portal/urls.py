from django.urls import path
from .views import profile
from . import views

app_name = 'portal'


urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login', views.BBLoginView, name='login'),
    path('', views.index, name='index'),
]
