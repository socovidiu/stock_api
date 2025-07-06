"""
Stock Sentiment & Trend Analysis API
====================================

This application provides a RESTful API to analyze stock market trends and sentiment
based on technical indicators and financial news. It integrates with the Alpha Vantage API
to fetch stock data and applies sentiment analysis on relevant news headlines.

Features:
---------
- Fetch and analyze stock trends using RSI, MACD, SMA, EMA, and Bollinger Bands.
- Perform sentiment analysis on news articles using VADER.
- Generate actionable stock recommendations (BUY, HOLD, SELL).
- Basic file-based user management (no database required).
- REST API endpoints documented with Swagger/OpenAPI.
- Auto-generated developer documentation using Sphinx.

Project Structure:
------------------
- `app.routes`: FastAPI routes for stock analysis and user operations.
- `app.services`: Business logic including external API integrations and analysis modules.
- `app.models`: Pydantic models for data validation.
- `app.db`: Simple file-based data storage for user data.

Tech Stack:
-----------
- Python 3.11+
- FastAPI
- Pydantic
- Alpha Vantage API
- VADER Sentiment
- Sphinx for documentation
- pytest for testing

Note:
-----
This is a portfolio/demo project and is not intended for production use. Some modules
(like user storage) are simplified for demonstration purposes.

Author: Your Name
"""
