# backend/predictor/apps.py
from django.apps import AppConfig
from pathlib import Path
import joblib, json
from sentence_transformers import SentenceTransformer     # pip install sentence-transformers

class PredictorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predictor"          # <- leave as-is (matches the folder name)

    def ready(self):
        base = Path(__file__).parent
        # 1️⃣  classifier weights
        self.clf = joblib.load(base / "clf.joblib")
        # 2️⃣  same Sentence-Transformer model used in training
        model_name = json.loads((base / "config.json").read_text())["sentence_model"]
        self.embedder = SentenceTransformer(model_name)
