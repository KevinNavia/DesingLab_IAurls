import re
from urllib.parse import urlparse

def validate_url(url: str) -> bool:
    """
    Validates if the given string is a valid URL.
    """
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None

def extract_url_features(url: str) -> dict:
    """
    Extracts features from a URL for ML classification.
    """
    parsed = urlparse(url)
    return {
        'length': len(url),
        'has_https': url.startswith('https'),
        'domain_length': len(parsed.netloc),
        'path_length': len(parsed.path),
        'query_length': len(parsed.query),
        'num_subdomains': len(parsed.netloc.split('.')) - 2 if parsed.netloc.count('.') > 1 else 0,
        'has_query': len(parsed.query) > 0,
        'has_fragment': len(parsed.fragment) > 0,
    }
