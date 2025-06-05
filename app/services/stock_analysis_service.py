"""
Stock Analysis Service

Handles market trend analysis, SMA data retrieval, and trade recommendations
using an injected stock data provider.
"""
import logging
from app.services.providers.base import StockDataProvider
from typing import Union, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StockAnalysisService:
    def __init__(self, provider: StockDataProvider):
        self.provider = provider

    def get_sma(self, symbol: str, period: int = 20) -> Union[Dict, str]:
        """
        Fetch the Simple Moving Average (SMA) for a stock.

        Returns last few SMA values or an error message.
        """
        return self.provider.get_sma(symbol, period)

    def get_rsi(self, symbol: str, period: int = 14):
        return self.provider.get_rsi(symbol, period)

    def analyze_trend(self, symbol: str) -> str:
        """
        Analyze market trend using RSI, MACD, and Bollinger Bands.

        Returns:
        -------
        str: One of "strong uptrend", "uptrend", "sideways", "downtrend", "strong downtrend", or "unknown"
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
        elif rsi > 70:
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
            return "strong uptrend"
        elif trend_score == 1:
            return "uptrend"
        elif trend_score == 0:
            return "sideways"
        elif trend_score == -1:
            return "downtrend"
        else:
            return "strong downtrend"

    def recommend_action(self, symbol: str) -> str:
        """
        Generate a stock recommendation based on technical trend and sentiment.

        Combines:
        - Technical analysis (MACD, RSI, Bollinger Bands) via `analyze_trend()`
        - News sentiment (positive vs negative mentions)

        Returns:
        -------
        str: "BUY", "SELL", or "HOLD"
        """
        trend = self.analyze_trend(symbol)
        news = self.provider.get_news_sentiment(symbol)

        logger.info(f"[{symbol}] Trend analysis result: {trend}")

        if isinstance(news, dict) and "error" in news:
            logger.warning(f"[{symbol}] Failed to fetch sentiment data: {news}")
            return "HOLD"

        # Sentiment analysis
        positive = sum(1 for n in news if n["sentiment"] == "positive")
        negative = sum(1 for n in news if n["sentiment"] == "negative")
        sentiment_score = positive - negative

        logger.info(f"[{symbol}] Sentiment score: +{positive} / -{negative} → net: {sentiment_score}")

        # Final recommendation
        if trend in ["strong uptrend", "uptrend"] and sentiment_score > 0:
            recommendation = "BUY"
        elif trend in ["strong downtrend", "downtrend"] and sentiment_score < 0:
            recommendation = "SELL"
        else:
            recommendation = "HOLD"

        logger.info(f"[{symbol}] Final recommendation: {recommendation}")
        return recommendation
