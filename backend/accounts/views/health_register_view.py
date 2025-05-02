from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from accounts.forms import HealthRegistrationForm

@csrf_exempt
def health_register_view(request):
    if request.method == 'POST':
        form = HealthRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Health registration submitted successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Send a POST request with health registration fields'})

