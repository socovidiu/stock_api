"""
Routes package for the Stock Sentiment & Trend Analysis API.

This package defines the HTTP API endpoints for interacting with the system's services.
Each module within this package handles a specific area of functionality such as
stock data, user management, or other domain-specific logic.

Submodules
----------
stock : Provides endpoints for retrieving and analyzing stock data.
users : Manages user-related operations such as creation and lookup.

Typical usage example:
----------------------
To register the routes with FastAPI:

    from app.routes import stock, users
    app.include_router(stock.router)
    app.include_router(users.router)
"""
