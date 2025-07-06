"""
Stock Data Provider Base Module

Defines the abstract base class `StockDataProvider` that outlines the required
interface for any stock data provider implementation.

This interface supports various technical indicators and sentiment analysis
retrieval based on stock symbols.

Classes
-------
StockDataProvider
    Abstract base class defining method signatures for stock analysis services.
"""

from abc import ABC, abstractmethod


class StockDataProvider(ABC):
    """
    Abstract base class for stock data providers.

    Any subclass must implement the methods for retrieving stock indicators and news sentiment.

    Methods
    -------
    get_sma(symbol: str, period: int = 20)
        Retrieve the Simple Moving Average (SMA) for a given symbol and period.

    get_ema(symbol: str, period: int = 10)
        Retrieve the Exponential Moving Average (EMA) for a given symbol and period.

    get_rsi(symbol: str, period: int = 14)
        Retrieve the Relative Strength Index (RSI) for a given symbol and period.

    get_bollinger_bands(symbol: str, period: int = 14, dev_up: int = 2, dev_down: int = 2)
        Retrieve the Bollinger Bands for a given symbol and period with specified deviations.

    get_news_sentiment(symbol: str)
        Retrieve news sentiment data for a given stock symbol.

    get_macd(symbol: str)
        Retrieve the Moving Average Convergence Divergence (MACD) data for a given symbol.
    """

    @abstractmethod
    def get_sma(self, symbol: str, period: int = 20):
        """
        Retrieve the Simple Moving Average (SMA).

        Parameters
        ----------
        symbol : str
            Stock ticker symbol (e.g., "AAPL").
        period : int, optional
            Period over which the SMA is calculated. Default is 20.

        Returns
        -------
        Any
            SMA data for the given stock symbol.
        """
        pass

    @abstractmethod
    def get_ema(self, symbol: str, period: int = 10):
        """
        Retrieve the Exponential Moving Average (EMA).

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : int, optional
            Period over which the EMA is calculated. Default is 10.

        Returns
        -------
        Any
            EMA data for the given stock symbol.
        """
        pass

    @abstractmethod
    def get_rsi(self, symbol: str, period: int = 14):
        """
        Retrieve the Relative Strength Index (RSI).

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : int, optional
            Period over which the RSI is calculated. Default is 14.

        Returns
        -------
        Any
            RSI data for the given stock symbol.
        """
        pass

    @abstractmethod
    def get_bollinger_bands(self, symbol: str, period: int = 14, dev_up: int = 2,
                            dev_down: int = 2):
        """
        Retrieve the Bollinger Bands.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : int, optional
            Period for the moving average. Default is 14.
        dev_up : int, optional
            Standard deviation above the mean. Default is 2.
        dev_down : int, optional
            Standard deviation below the mean. Default is 2.

        Returns
        -------
        Any
            Bollinger Bands data.
        """
        pass

    @abstractmethod
    def get_news_sentiment(self, symbol: str):
        """
        Retrieve news sentiment data for a given stock symbol.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.

        Returns
        -------
        Any
            News sentiment analysis results.
        """
        pass

    @abstractmethod
    def get_macd(self, symbol: str) -> dict:
        """
        Retrieve the Moving Average Convergence Divergence (MACD).

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.

        Returns
        -------
        dict
            Dictionary containing MACD and signal line data.
        """
        pass
