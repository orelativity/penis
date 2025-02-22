import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import string

# Ensure NLP resources are available
nltk.download("punkt")
nltk.download("stopwords")

# AI Companies List for tracking mentions
AI_COMPANIES = ["OpenAI", "Google", "Microsoft", "NVIDIA", "Meta", "Amazon", "Anthropic", "Tesla", "IBM", "Apple"]

def extract_keywords(news_articles):
    """Extracts the top AI-related keywords from news headlines."""
    text = " ".join(article["title"] for article in news_articles)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("english") + list(string.punctuation))
    words = [word for word in words if word not in stop_words and word.isalpha()]

    return Counter(words).most_common(10)

def analyze_sentiment(news_articles):
    """Performs sentiment analysis on news headlines."""
    sentiment_scores = {"positive": 0, "neutral": 0, "negative": 0}

    for article in news_articles:
        analysis = TextBlob(article["title"])
        sentiment = analysis.sentiment.polarity

        if sentiment > 0:
            sentiment_scores["positive"] += 1
        elif sentiment < 0:
            sentiment_scores["negative"] += 1
        else:
            sentiment_scores["neutral"] += 1

    total = sum(sentiment_scores.values())
    return {k: round((v / total) * 100, 2) for k, v in sentiment_scores.items()} if total > 0 else sentiment_scores

def extract_companies(news_articles):
    """Finds frequently mentioned AI companies in news headlines."""
    company_mentions = {company: 0 for company in AI_COMPANIES}

    for article in news_articles:
        for company in AI_COMPANIES:
            if company.lower() in article["title"].lower():
                company_mentions[company] += 1

    return {k: v for k, v in company_mentions.items() if v > 0}

def calculate_ai_market_score(sentiment_results, keywords, company_trends):
    """Calculates AI Market Score based on sentiment, keywords, and company mentions."""
    positive_sentiment = sentiment_results.get("positive", 0)
    keyword_mentions = sum(dict(keywords).values())
    company_mentions = sum(company_trends.values())

    # Normalize values to fit the score system
    sentiment_weight = positive_sentiment * 0.5
    keyword_weight = min(keyword_mentions, 100) * 0.3
    company_weight = min(company_mentions, 50) * 0.2

    return round(sentiment_weight + keyword_weight + company_weight, 2)
