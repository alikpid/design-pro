from django.urls import path
from . import views
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView

app_name = 'portal'


urlpatterns = [
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('', views.index, name='index'),
]

