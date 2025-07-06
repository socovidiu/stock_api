"""
Stock Analysis Service Module

This module defines the StockAnalysisService class, which provides methods
for analyzing market trends and generating trading recommendations using
technical indicators and news sentiment data.

The service relies on an injected data provider that implements the
StockDataProvider interface.
"""

from typing import Union, Dict
from app.services.providers.base import StockDataProvider

class StockAnalysisService:
    """
    A service for performing stock market trend analysis and providing trade recommendations.

    Attributes
    ----------
    provider : StockDataProvider
        An injected data provider for retrieving technical indicators and sentiment data.
    """

    def __init__(self, provider: StockDataProvider):
        """
        Initialize the analysis service with a stock data provider.

        Parameters
        ----------
        provider : StockDataProvider
            An instance of a provider implementing the StockDataProvider interface.
        """
        self.provider = provider

    def get_sma(self, symbol: str, period: int = 20) -> Union[Dict, str]:
        """
        Retrieve the Simple Moving Average (SMA) for a given stock.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : int, optional
            Number of days for the SMA period (default is 20).

        Returns
        -------
        dict or str
            Dictionary containing SMA values or an error message.
        """
        return self.provider.get_sma(symbol, period)

    def get_rsi(self, symbol: str, period: int = 14):
        """
        Retrieve the Relative Strength Index (RSI) for a given stock.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : int, optional
            Number of days for the RSI period (default is 14).

        Returns
        -------
        float or None
            RSI value, or None if unavailable.
        """
        return self.provider.get_rsi(symbol, period)

    def analyze_trend(self, symbol: str) -> str:
        """
        Analyze the current market trend using RSI, MACD, and Bollinger Bands.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.

        Returns
        -------
        str
            One of "strong uptrend", "uptrend", "sideways", "downtrend",
            "strong downtrend", or "unknown".
        """
        rsi = self.provider.get_rsi(symbol)
        macd = self.provider.get_macd(symbol)
        bbands = self.provider.get_bollinger_bands(symbol)

        if rsi is None or macd is None or bbands is None:
            return "unknown"

        trend_score = 0

        # RSI: Overbought/Oversold
        if rsi < 30:
            trend_score += 1  # Bullish
        if rsi > 70:
            trend_score -= 1  # Bearish

        # MACD Signal
        if macd["macd"] > macd["signal"]:
            trend_score += 1
        else:
            trend_score -= 1

        # Bollinger Band: Price crossing upper/lower band
        if bbands["middle"] > bbands["upper"]:
            trend_score -= 1
        elif bbands["middle"] < bbands["lower"]:
            trend_score += 1

        # Final classification
        if trend_score >= 2:
            trend_result = "strong uptrend"
        elif trend_score == 1:
            trend_result = "uptrend"
        elif trend_score == 0:
            trend_result = "sideways"
        elif trend_score == -1:
            trend_result = "downtrend"
        else:
            trend_result = "strong downtrend"

        return trend_result

    def recommend_action(self, symbol: str) -> str:
        """
        Generate a stock recommendation based on trend analysis and sentiment.

        Combines technical trend indicators and sentiment analysis to classify
        the recommendation as "BUY", "SELL", or "HOLD".

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.

        Returns
        -------
        str
            Recommendation string: "BUY", "SELL", or "HOLD".
        """
        trend = self.analyze_trend(symbol)
        news = self.provider.get_news_sentiment(symbol)

        if isinstance(news, dict) and "error" in news:
            return "HOLD"

        positive = sum(1 for n in news if n["sentiment"] == "positive")
        negative = sum(1 for n in news if n["sentiment"] == "negative")
        sentiment_score = positive - negative

        if trend in ["strong uptrend", "uptrend"] and sentiment_score > 0:
            return "BUY"
        if trend in ["strong downtrend", "downtrend"] and sentiment_score < 0:
            return "SELL"
        return "HOLD"
