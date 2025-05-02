# backend/predictor/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.apps import apps
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")   # middleware bypass
class PredictView(APIView):
    authentication_classes = []      # ⬅️  turn off SessionAuthentication
    permission_classes      = [AllowAny]

    """
    POST /api/predict/
    Body: { "text": "runny nose and sore throat" }
    """
    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "Missing 'text' field."},
                            status=status.HTTP_400_BAD_REQUEST)

        cfg   = apps.get_app_config("predictor")
        emb   = cfg.embedder.encode([text])
        proba = cfg.clf.predict_proba(emb)[0]

        top3 = sorted(zip(cfg.clf.classes_, proba),
                      key=lambda x: x[1], reverse=True)[:3]

        return Response({
            "top_prediction": top3[0][0],
            "alternatives": [
                {"disease": d, "probability": round(p, 4)} for d, p in top3
            ]
        })
