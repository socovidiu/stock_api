"""
Providers Package

This package defines the interface and concrete implementations for external data providers.

Modules
-------
- base : Abstract base class (StockDataProvider) that defines the interface for data providers.
- alpha_vantage : AlphaVantageAdapter class that implements the provider interface using Alpha Vantage's API.

Purpose
-------
These providers encapsulate the logic for fetching stock data, technical indicators,
and sentiment analysis from third-party APIs, ensuring that the rest of the application
remains decoupled from specific data sources.

Usage
-----
The service layer (e.g., NewsService, StockAnalysisService) depends on the abstract
StockDataProvider interface and can work with any implementation.
"""
