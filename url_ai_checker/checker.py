import requests
from .model.classifier import UrlClassifier

class UrlAIChecker:
    def __init__(self):
        self.model = UrlClassifier()

    def check_url(self, url: str) -> dict:
        try:
            response = requests.get(url, timeout=3)
            status = response.status_code
        except Exception:
            status = None
        ai_result = self.model.predict(url, status)
        return {"url": url, "http_status": status, "ai_status": ai_result}
