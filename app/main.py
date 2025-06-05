"""
Main Application Entry Point

This module initializes the FastAPI app, registers route modules,
and provides a root endpoint for the Stock Sentiment Analysis API.

Modules:
- app.routes.stock  → Handles stock news and recommendations
- app.routes.users  → Handles basic user operations
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import stock, users

# Initialize the FastAPI application
app = FastAPI(
    title="Stock Sentiment Analysis API",
    description="Provides stock news, sentiment analysis, and trading recommendations.",
    version="1.0.0"
)

# CORS configuration
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-frontend-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(stock.router, prefix="/stock", tags=["Stock"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    """
    Root endpoint to verify that the API is running.

    Returns:
    -------
    dict
        A welcome message.
    """
    return {"message": "Welcome to the Stock Sentiment Analysis API!"}
