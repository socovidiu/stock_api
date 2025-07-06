"""
News Service Module

This module defines the NewsService class, responsible for retrieving
financial news and performing sentiment analysis on it.

It utilizes a pluggable stock data provider (e.g., Alpha Vantage) that
implements the `StockDataProvider` interface to fetch news sentiment data.
"""

from typing import Union, List, Dict
from app.services.providers.base import StockDataProvider


class NewsService:
    """
    Service class for retrieving and analyzing stock-related news.

    This service acts as a wrapper around a stock data provider,
    exposing functionality for retrieving sentiment-enriched news articles.
    """

    def __init__(self, provider: StockDataProvider):
        """
        Initialize the NewsService.

        Parameters
        ----------
        provider : StockDataProvider
            An instance of a class implementing the StockDataProvider interface,
            used to fetch stock news sentiment.
        """
        self.provider = provider

    def get_news(self, symbol: str) -> Union[List[Dict], Dict]:
        """
        Fetch news and sentiment analysis for a given stock symbol.

        Parameters
        ----------
        symbol : str
            The stock ticker symbol (e.g., "AAPL", "TSLA").

        Returns
        -------
        Union[List[Dict], Dict]
            A list of news articles with sentiment scores, or
            an error dictionary if the fetch fails.
        """
        return self.provider.get_news_sentiment(symbol)
