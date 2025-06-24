# 📊 Stock Sentiment & Trend Analysis API

This project is a FastAPI-based backend service that provides stock-related insights using real-time financial data and news sentiment analysis. It integrates with Alpha Vantage to retrieve market indicators like RSI, MACD, Bollinger Bands, and more.

---

## 🚀 Features

- ✅ Fetch recent news for a stock and perform sentiment analysis
- 📈 Analyze market trends using technical indicators (RSI, MACD, BBANDS)
- 💡 Generate trading recommendations: **BUY**, **SELL**, or **HOLD**
- 🧪 Built-in support for testing with `pytest`
- 🔒 File-based user system (for demo purposes)
- 🔧 Modular architecture with adapter pattern for data providers

---

## 🧠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – for API development
- [Pydantic](https://pydantic-docs.helpmanual.io/) – data validation
- [Uvicorn](https://www.uvicorn.org/) – ASGI server
- [Alpha Vantage API](https://www.alphavantage.co/) – market & news data
- [NLTK + VADER](https://github.com/cjhutto/vaderSentiment) – sentiment analysis
- [Pytest](https://docs.pytest.org/) – testing framework

---

## 📂 Project Structure

```bash
.
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── routes/               # API routes
│   ├── services/             # Business logic + providers
│   ├── models/               # Pydantic models
│   ├── db/                   # JSON file-based user store
│   ├── config.py             # Active provider definitions
├── tests/                    # Unit tests
├── .env                      # API keys and secrets
├── requirements.txt
├── README.md
```
## Using stock_api

To use stock_api, follow these steps:

Requirements installation:
```
pip install -r requirements.txt
```
Create .env file
```
ALPHA_NEWS_KEY=your_alpha_vantage_api_key
```

Running the App:
```
uvicorn app.main:app --reload
```

Visit the interactive API docs at:
```
📍 http://127.0.0.1:8000/docs
```
