import pytest
from url_ai_checker import UrlAIChecker

def test_check_url_structure():
    checker = UrlAIChecker()
    result = checker.check_url("https://www.google.com")
    assert "url" in result
    assert "http_status" in result
    assert "ai_status" in result
    assert isinstance(result["http_status"], int) or result["http_status"] is None
    assert isinstance(result["ai_status"], str)

def test_check_url_no_response():
    checker = UrlAIChecker()
    result = checker.check_url("http://invalid.domain.nonexistent")
    assert result["http_status"] is None
    assert result["ai_status"] == "no_response"

def test_check_url_with_timeout():
    checker = UrlAIChecker()
    # Use a URL that might be slow but should respond
    result = checker.check_url("https://httpbin.org/delay/1")
    assert "url" in result
    assert "http_status" in result
    assert "ai_status" in result
