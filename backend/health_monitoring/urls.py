from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def live_view(request):
    return HttpResponse("✅ Backend is live and working!")

urlpatterns = [
    path('', live_view),  # ✅ Root route for /
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("api/", include("predictor.urls")),
]
