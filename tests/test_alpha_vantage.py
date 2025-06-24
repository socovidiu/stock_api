import pytest
import requests
from app.services.providers.alpha_vantage import AlphaVantageAdapter

MOCK_RESPONSE = {
    "Time Series (Daily)": {
        "2024-06-01": {"4. close": "100.0"},
        "2024-06-02": {"4. close": "102.0"},
        "2024-06-03": {"4. close": "104.0"},
        "2024-06-04": {"4. close": "106.0"},
        "2024-06-05": {"4. close": "108.0"},
        "2024-06-06": {"4. close": "110.0"},
        "2024-06-07": {"4. close": "112.0"},
        "2024-06-08": {"4. close": "114.0"},
        "2024-06-09": {"4. close": "116.0"},
        "2024-06-10": {"4. close": "118.0"},
        "2024-06-11": {"4. close": "120.0"},
        "2024-06-12": {"4. close": "122.0"},
        "2024-06-13": {"4. close": "124.0"},
        "2024-06-14": {"4. close": "126.0"},
        "2024-06-15": {"4. close": "128.0"},
        "2024-06-16": {"4. close": "130.0"},
        "2024-06-17": {"4. close": "132.0"},
        "2024-06-18": {"4. close": "134.0"},
        "2024-06-19": {"4. close": "136.0"},
        "2024-06-20": {"4. close": "138.0"},
        "2024-06-21": {"4. close": "140.0"},
        "2024-06-22": {"4. close": "142.0"},
        "2024-06-23": {"4. close": "144.0"},
        "2024-06-24": {"4. close": "146.0"},
        "2024-06-25": {"4. close": "148.0"},
        "2024-06-26": {"4. close": "150.0"}
    }
}

@pytest.fixture
def adapter():
    return AlphaVantageAdapter()

def test_get_macd(monkeypatch, adapter):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return MOCK_RESPONSE
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = adapter.get_macd("TSLA")
    assert isinstance(result, dict)
    assert "macd" in result
    assert "signal" in result
    assert isinstance(result["macd"], float)
