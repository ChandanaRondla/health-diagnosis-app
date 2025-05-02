from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("✅ Django backend is running!")

urlpatterns = [
    path('', home_view),  # ✅ Root route
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),              
    path('accounts/', include('django.contrib.auth.urls')),   # Built-in login/logout
    path("api/", include("predictor.urls")),
]
