"""
News Service Module

Uses an injected stock data provider to fetch and analyze news sentiment.
"""

from app.services.providers.base import StockDataProvider
from typing import Union, List, Dict

class NewsService:
    def __init__(self, provider: StockDataProvider):
        """
        Initializes the service with a data provider.

        Parameters:
        ----------
        provider : StockDataProvider
            Any implementation of the StockDataProvider interface.
        """
        self.provider = provider

    def get_news(self, symbol: str) -> Union[List[Dict], Dict]:
        """
        Fetch news and sentiment for a stock symbol.

        Parameters:
        ----------
        symbol : str
            Stock ticker symbol (e.g., "AAPL", "TSLA").

        Returns:
        -------
        list of dict or dict
            A list of news items with sentiment, or an error response.
        """
        return self.provider.get_news_sentiment(symbol)
