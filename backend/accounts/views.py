from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
import json
import traceback
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                "success": False,
                "message": "Invalid JSON format"
            }, status=400)
        
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')

        # Basic validation
        if not username or not email or not password1 or not password2:
            return JsonResponse({
                "success": False,
                "message": "All fields are required."
            }, status=400)

        if password1 != password2:
            return JsonResponse({
                "success": False,
                "message": "Passwords do not match."
            }, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success": False,
                "message": "Username already exists."
            }, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({
                "success": False,
                "message": "Email already exists."
            }, status=400)

        # Validate password strength
        try:
            validate_password(password1)
        except ValidationError as e:
            return JsonResponse({
                "success": False,
                "message": e.messages  # return as list
            }, status=400)

        try:
            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            user.save()

            # Optional: Auto-login after registration
            login(request, user)

            return JsonResponse({
                "success": True,
                "message": f"User {username} registered successfully.",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            }, status=201)

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({
                "success": False,
                "message": f"Server error: {str(e)}"
            }, status=500)

    else:
        return JsonResponse({
            "success": False,
            "message": "Only POST method is allowed."
        }, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password = data.get('password', '')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Create a dummy token for now
                token = f"dummy_token_{username}_{user.id}"

                return JsonResponse({
                    "success": True,
                    "message": "Login successful.",
                    "token": token,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    }
                })
            else:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid credentials."
                }, status=400)

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({
                "success": False,
                "message": f"Server error: {str(e)}"
            }, status=500)

    else:
        return JsonResponse({
            "success": False,
            "message": "Only POST method is allowed."
        }, status=405)
