"""
Service Registry
================

This module initializes and exposes shared service instances for use across the application.

Services
--------
- AlphaVantageAdapter : Provides access to Alpha Vantage API data.
- NewsService : Handles fetching and analyzing stock-related news.
- StockAnalysisService : Offers analysis and recommendations based on stock trends.

Examples
--------
Import shared services:

    from app.services.registry import ACTIVE_NEWS_PROVIDER, ACTIVE_ANALYSIS_PROVIDER
"""
from app.services.providers.alpha_vantage import AlphaVantageAdapter
from app.services.news_service import NewsService
from app.services.stock_analysis_service import StockAnalysisService

# Shared provider
ALPHA_PROVIDER = AlphaVantageAdapter()

# Services
ACTIVE_NEWS_PROVIDER = NewsService(ALPHA_PROVIDER)
ACTIVE_ANALYSIS_PROVIDER = StockAnalysisService(ALPHA_PROVIDER)

# for testing
# mock_service = NewsService(MockProvider())
