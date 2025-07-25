
import os

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
PYTHON_VERSION = os.getenv("PYTHON_VERSION", "3.10")
MODEL_THRESHOLD = float(os.getenv("MODEL_THRESHOLD", "0.75"))
GOOGLE_SHEET_API_KEY = os.getenv("GOOGLE_SHEET_API_KEY", None)
