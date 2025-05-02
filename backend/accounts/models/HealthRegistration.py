from django.db import models
from django.contrib.auth.models import User  # ✅ import User model

class HealthRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ add this line

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    pincode = models.CharField()
    residential_address = models.TextField()
    known_allergies = models.TextField(blank=True)
    existing_conditions = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    past_surgeries = models.TextField(blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.user.username})"

