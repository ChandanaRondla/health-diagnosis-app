from django import forms
from accounts.models import HealthRegistration

class HealthRegistrationForm(forms.ModelForm):
    class Meta:
        model = HealthRegistration
        fields = [
            'full_name',
            'date_of_birth',
            'gender',
            'contact_number',
            'email',
            'residential_address',
            'known_allergies',
            'existing_conditions',
            'current_medications',
            'pincode',
            'past_surgeries',

        ]
