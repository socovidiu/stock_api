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