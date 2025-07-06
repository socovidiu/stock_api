"""
Alpha Vantage Adapter Module

This module provides an implementation of the `StockDataProvider` interface using the Alpha Vantage API.
It supports fetching various stock indicators such as SMA, EMA, RSI, Bollinger Bands, MACD, and sentiment-analyzed news articles.

Classes
-------
AlphaVantageAdapter
    Adapter class that fetches stock indicators and news sentiment using Alpha Vantage endpoints.
"""
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from app.services.sentiment import analyze_sentiment
from .base import StockDataProvider

load_dotenv()
API_KEY = os.getenv("ALPHA_NEWS_KEY")


class AlphaVantageAdapter(StockDataProvider):
    """
    Alpha Vantage implementation of the StockDataProvider interface.

    Provides methods to fetch various technical indicators and news sentiment data
    for a given stock symbol by communicating with the Alpha Vantage API.

    Methods
    -------
    get_sma(symbol, period)
        Fetch Simple Moving Average values.

    get_ema(symbol, period)
        Fetch Exponential Moving Average values.

    get_rsi(symbol, period)
        Fetch Relative Strength Index values.

    get_bollinger_bands(symbol, period, dev_up, dev_down)
        Fetch Bollinger Bands data.

    get_news_sentiment(symbol)
        Fetch and analyze sentiment from recent news articles.

    get_macd(symbol)
        Calculate MACD and signal line values from historical prices.
    """

    BASE_URL = "https://www.alphavantage.co/query"
    DEFAULT_TIMEOUT = 10  # seconds

    def get_sma(self, symbol: str, period: int = 20):
        """
        Fetch the Simple Moving Average (SMA) for a stock symbol.

        Parameters:
        ----------
        symbol : str
            Stock ticker symbol.
        period : int
            Number of days used to calculate the SMA (default is 20).

        Returns:
        -------
        dict
            SMA values with latest 5 dates, or error info.
        """
        params = {
            "function": "SMA",
            "symbol": symbol,
            "interval": "daily",
            "time_period": period,
            "series_type": "close",
            "apikey": API_KEY,
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT).json()

        try:
            sma_data = response["Technical Analysis: SMA"]
            sorted_data = sorted(sma_data.items(), reverse=True)[:5]
            return {"status": "ok", "data": sorted_data}
        except KeyError:
            return {"status": "error", "details": response}

    def get_ema(self, symbol: str, period: int = 10):
        """
        Fetch the Exponential Moving Average (EMA)  for a stock symbol.

        Parameters:
        ----------
        symbol : str
            Stock ticker symbol.
        period : int
            Number of days used to calculate the EMA.

        Returns:
        -------
        dict
            EMA values, or error info.
        """
        params = {
            "function": "EMA",
            "symbol": symbol,
            "interval": "daily",
            "time_period": period,
            "series_type": "close",
            "apikey": API_KEY,
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT).json()

        try:
            ema_data = response["Technical Analysis: EMA"]
            sorted_data = sorted(ema_data.items(), reverse=True)[:5]
            return {"status": "ok", "data": sorted_data}
        except KeyError:
            return {"status": "error", "details": response}

    def get_rsi(self, symbol: str, period: int = 14):
        """
        Fetch the Relative Strength Index (RSI) for a stock symbol.

        Parameters:
        ----------
        symbol : str
            Stock ticker symbol.
        period : int
            Number of days used to calculate the RSI.

        Returns:
        -------
        dict
            RSI values, or error info.
        """
        params = {
            "function": "RSI",
            "symbol": symbol,
            "interval": "daily",
            "time_period": period,
            "series_type": "close",
            "apikey": API_KEY,
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT).json()

        try:
            rsi_data = response["Technical Analysis: RSI"]
            sorted_data = sorted(rsi_data.items(), reverse=True)
            # return {"status": "ok", "data": sorted_data}
            latest_rsi = float(sorted_data[0][1]["RSI"])
            return latest_rsi
        except (KeyError, IndexError, ValueError):
            return None

    def get_bollinger_bands(
        self, symbol: str, period: int = 20, dev_up: int = 2, dev_down: int = 2
    ):
        """
        Fetch the Bollinger bands (BBANDS) for a stock symbol.

        Parameters:
        ----------
        symbol : str
            Stock ticker symbol.
        period : int
            Number of days used to calculate the Bollinger Bands.

        Returns:
        -------
        dict
            Bollinger Bands values, or error info.
        """
        params = {
            "function": "BBANDS",
            "symbol": symbol,
            "interval": "daily",
            "time_period": period,
            "series_type": "close",
            "nbdevup": dev_up,
            "nbdevdn": dev_down,
            "apikey": API_KEY,
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT).json()

        try:
            bb_data = response["Technical Analysis: BBANDS"]
            sorted_data = sorted(bb_data.items(), reverse=True)
            latest = sorted_data[0][1]

            return {
                "upper": float(latest["Real Upper Band"]),
                "middle": float(latest["Real Middle Band"]),
                "lower": float(latest["Real Lower Band"]),
                "date": sorted_data[0][0],
            }
        except (KeyError, IndexError, ValueError):
            return None

    def get_news_sentiment(self, symbol: str):
        """
        Fetches and analyzes news related to a stock symbol using Alpha Vantage's News Sentiment API.

        For each article, the title is analyzed for sentiment using VADER,
        and a list of structured news items is returned.

        Parameters:
        ----------
        symbol : str
            The stock ticker symbol to fetch news for (e.g., 'AAPL', 'TSLA').

        Returns:
        -------
        list[dict] or dict
            A list of news items with title, link, published date, and sentiment.
            If the API response is invalid, a dictionary with an error message is returned.
        """
        params = {"function": "NEWS_SENTIMENT", "tickers": symbol, "apikey": API_KEY}
        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT)
        data = response.json()

        # Check if the response includes expected data
        if "feed" not in data:
            return {"error": "Failed to fetch news", "details": data}

        news_list = []
        for item in data.get("feed", []):
            news_item = {
                "title": item["title"],
                "link": item["url"],
                "published": item["time_published"],
                "sentiment": analyze_sentiment(item["title"]),
            }
            news_list.append(news_item)

        return news_list

    def get_macd(self, symbol: str):
        """
        Calculate MACD and signal line using closing prices.

        Args:
        symbol (str): Stock ticker symbol.

        Returns:
            dict: Latest MACD and signal line values.
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "compact",
            "apikey": API_KEY,
        }

        response = requests.get(self.BASE_URL, params=params, timeout=self.DEFAULT_TIMEOUT)
        response.raise_for_status()
        data = response.json()

        if "Error Message" in data or "Note" in data:
            print(f"[ERROR] API response error for symbol '{symbol}': {data}")
            return None

        ts = data["Time Series (Daily)"]
        closes = [float(v["4. close"]) for k, v in sorted(ts.items())]
        df = pd.Series(closes)

        ema12 = df.ewm(span=12, adjust=False).mean()
        ema26 = df.ewm(span=26, adjust=False).mean()
        macd_line = ema12 - ema26
        signal_line = macd_line.ewm(span=9, adjust=False).mean()

        return {
            "macd": round(macd_line.iloc[-1], 4),
            "signal": round(signal_line.iloc[-1], 4),
        }
