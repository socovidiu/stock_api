# app/services/providers/base.py
from abc import ABC, abstractmethod

class StockDataProvider(ABC):
    @abstractmethod
    def get_sma(self, symbol: str, period: int = 20):
        pass

    @abstractmethod
    def get_ema(self, symbol: str, period: int = 10):
        pass

    @abstractmethod
    def get_rsi(self, symbol: str, period: int = 14):
        pass

    @abstractmethod
    def get_bollinger_bands(self, symbol: str, period: int  = 14, dev_up: int = 2, dev_down: int = 2):
        pass

    @abstractmethod
    def get_news_sentiment(self, symbol: str):
        pass

    @abstractmethod
    def get_macd(self, symbol: str) -> dict:
        pass