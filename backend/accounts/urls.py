from django.urls import path
from accounts.views import (
    register_view,
    health_register_view,
    health_register_get_view,
    login_view)



urlpatterns = [
    path('register/', register_view, name='register'),
    path('health/register/', health_register_view, name='health-register'),
    path('login/', login_view, name='login'),
    path('health/', health_register_get_view, name='health-register-get'),
]
