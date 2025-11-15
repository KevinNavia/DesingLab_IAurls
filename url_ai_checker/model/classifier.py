import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ..utils.helpers import extract_url_features

class UrlClassifier:
    def __init__(self):
        # Dummy training data for demonstration
        # In a real scenario, this would be trained on a large dataset
        self.model = self._train_dummy_model()

    def _train_dummy_model(self):
        # Create dummy features and labels
        features = []
        labels = []
        # Healthy URLs
        healthy_urls = [
            "https://www.google.com",
            "https://github.com",
            "https://stackoverflow.com"
        ]
        for url in healthy_urls:
            features.append(list(extract_url_features(url).values()))
            labels.append(1)  # 1 for healthy

        # Unhealthy URLs (simulate with variations)
        unhealthy_urls = [
            "http://invalid.domain",
            "https://fake-site.com/bad",
            "http://localhost:9999/nonexistent"
        ]
        for url in unhealthy_urls:
            features.append(list(extract_url_features(url).values()))
            labels.append(0)  # 0 for unhealthy

        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(features, labels)
        return model

    def predict(self, url, http_status):
        # Fallback to status-based logic if model fails
        if http_status is None:
            return "no_response"
        if 200 <= http_status < 400:
            return "healthy"
        if 400 <= http_status < 500:
            return "client_error"
        return "server_error"

        # Use ML model for prediction (commented out as it may not be accurate with dummy data)
        # features = np.array(list(extract_url_features(url).values())).reshape(1, -1)
        # prediction = self.model.predict(features)[0]
        # return "healthy" if prediction == 1 else "unhealthy"
