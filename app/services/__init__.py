"""
Services Package

This package contains the core business logic of the Stock Sentiment & Trend Analysis API.

Modules:
- `stock_analysis_service.py`: Provides trend analysis and trading recommendations based on stock data.
- `news_service.py`: Fetches and processes stock-related news articles.
- `sentiment.py`: Performs sentiment analysis on financial news headlines.
- `users_service.py`: Manages user-related logic and operations.
- `providers/`: Contains provider adapters (e.g., Alpha Vantage) used across services.

These services are designed to be reusable and loosely coupled with the external API routes.
"""
