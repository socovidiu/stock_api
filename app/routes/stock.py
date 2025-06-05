"""
Stock Routes Module

This module defines API endpoints related to stock market data, including:
- Retrieving recent news articles with sentiment analysis
- Fetching Simple Moving Average (SMA) values
- Providing trade recommendations based on market trends and sentiment

Routes:
-------
- GET /stock/news/{stock_symbol}
    → News with sentiment analysis for the given stock symbol

- GET /stock/recommend/{stock_symbol}
    → Trade recommendation: BUY, SELL, or HOLD

- GET /stock/sma/{stock_symbol}
    → Recent Simple Moving Average values for the stock
"""

from fastapi import APIRouter
from app.config import ACTIVE_NEWS_PROVIDER, ACTIVE_ANALYSIS_PROVIDER

router = APIRouter()

@router.get("/news/{stock_symbol}")
def get_news(stock_symbol: str):
    """
    Fetch recent news and sentiment analysis for a specific stock symbol.

    Parameters:
    ----------
    stock_symbol : str
        The stock ticker symbol (e.g., 'AAPL', 'TSLA').

    Returns:
    -------
    dict
        Contains the stock symbol and a list of news articles with sentiment.
    """
    news = ACTIVE_NEWS_PROVIDER.get_news(stock_symbol)
    return {"stock_symbol": stock_symbol, "news": news}


@router.get("/recommend/{stock_symbol}")
def get_recommendation(stock_symbol: str):
    """
    Generate a trading recommendation based on sentiment and market trend.

    Parameters:
    ----------
    stock_symbol : str
        The stock ticker symbol.

    Returns:
    -------
    dict
        A dictionary with the recommendation result:
        - "BUY", "SELL", or "HOLD"
    """
    action = ACTIVE_ANALYSIS_PROVIDER.recommend_action(stock_symbol)
    return {"stock_symbol": stock_symbol, "recommendation": action}


@router.get("/sma/{stock_symbol}")
def get_sma(stock_symbol: str):
    """
    Retrieve the Simple Moving Average (SMA) values for a stock.

    Parameters:
    ----------
    stock_symbol : str
        The stock ticker symbol.

    Returns:
    -------
    dict
        A dictionary containing the stock symbol and the most recent SMA data.
    """
    sma = ACTIVE_ANALYSIS_PROVIDER.get_sma(stock_symbol)
    return {"stock_symbol": stock_symbol, "sma": sma}
