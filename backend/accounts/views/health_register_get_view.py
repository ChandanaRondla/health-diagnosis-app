from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import HealthRegistration

@login_required
def health_register_get_view(request):
    if request.method == 'GET':
        try:
            health = HealthRegistration.objects.get(user=request.user)
            data = {
                "full_name": health.full_name,
                "date_of_birth": str(health.date_of_birth),
                "gender": health.gender,
                "contact_number": health.contact_number,
                "email": health.email,
                "residential_address": health.residential_address,
                "known_allergies": health.known_allergies,
                "existing_conditions": health.existing_conditions,
                "current_medications": health.current_medications,
                "past_surgeries": health.past_surgeries,
                "registered_at": str(health.registered_at),
            }
            return JsonResponse(data)
        except HealthRegistration.DoesNotExist:
            return JsonResponse({"error": "No health data found."}, status=404)
    return JsonResponse({'message': 'Only GET allowed on this route'}, status=405)
