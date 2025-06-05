"""
Sentiment Analysis Service

This module uses the NLTK VADER sentiment analyzer to evaluate the sentiment
of given text content. It classifies text as 'positive', 'neutral', or 'negative'
based on the compound score.

Dependencies:
- nltk
- vader_lexicon (downloaded automatically if missing)
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure VADER lexicon is available
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')


def analyze_sentiment(text: str) -> str:
    """
    Analyzes the sentiment of a given text using NLTK's VADER sentiment analyzer.

    Parameters:
    ----------
    text : str
        The input string to analyze (e.g., news headline, tweet, comment)

    Returns:
    -------
    str
        Sentiment classification:
        - "positive" if compound score > 0.1
        - "negative" if compound score < -0.1
        - "neutral" otherwise
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)["compound"]

    if sentiment_score > 0.1:
        return "positive"
    elif sentiment_score < -0.1:
        return "negative"
    else:
        return "neutral"
