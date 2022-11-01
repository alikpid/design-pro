from django.urls import path
from .views import index
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import detail

app_name = 'portal'


urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('', index, name='index'),
]

