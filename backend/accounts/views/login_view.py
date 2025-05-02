from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            # Print raw request body for debugging
            print("Raw request body:", request.body.decode('utf-8'))
            
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            print(f"Login attempt for user: {username}")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                print(f"User {username} authenticated successfully")
                return JsonResponse({
                    'status': 'success',
                    'token': 'dummy_token',  # You'd use a real token in production
                    'message': f"User {username} logged in."
                })
            else:
                print(f"Authentication failed for user: {username}")
                return JsonResponse({
                    'status': 'error',
                    'message': 'Invalid credentials'
                }, status=401)
        except Exception as e:
            print(f"Exception in login_view: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'message': f"Login error: {str(e)}"
            }, status=500)
    return JsonResponse({"message": "Please use POST method"}, status=405)
