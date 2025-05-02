from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON format"}, status=400)
        
        username = data.get('username', '')
        email = data.get('email', '')
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')

        if not username or not email or not password1 or not password2:
            return JsonResponse({"success": False, "message": "All fields are required."}, status=400)
        
        if password1 != password2:
            return JsonResponse({"success": False, "message": "Passwords do not match."}, status=400)

        try:
            validate_password(password1)
        except ValidationError as e:
            return JsonResponse({"success": False, "message": e.messages}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already taken."}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email already registered."}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user)

        return JsonResponse({"success": True, "message": "User registered successfully."}, status=201)

    else:
        return JsonResponse({"success": False, "message": "Only POST method allowed."}, status=405)
