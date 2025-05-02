from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),              # ✅ Your app’s URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path("api/", include("predictor.urls")),# ✅ Built-in login/logout
]
