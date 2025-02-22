from news_fetcher import get_news
from ai_market_analysis import extract_keywords, analyze_sentiment, extract_companies, calculate_ai_market_score
from telegram_alerts import send_telegram_message

def main():
    news_articles = get_news()

    if not news_articles:
        print("No AI news articles found.")
        return

    print("\nLatest AI News:")
    for article in news_articles[:5]:  
        print(f"{article['title']} - {article['url']}")

    keywords = extract_keywords(news_articles)
    sentiment_results = analyze_sentiment(news_articles)
    company_trends = extract_companies(news_articles)

    ai_market_score = calculate_ai_market_score(sentiment_results, keywords, company_trends)
    print(f"\nAI Market Score: {ai_market_score}")

    # Define message based on AI Market Score
    if ai_market_score > 80:
        message = f"🚀 AI Market is HOT! 🔥 Score: {ai_market_score}"
    elif 50 <= ai_market_score <= 79:
        message = f"⚖️ AI Market is Stable. Score: {ai_market_score}"
    else:
        message = f"❌ AI Market is Cooling Down. Score: {ai_market_score}"

    send_telegram_message(message)

if __name__ == "__main__":
    main()
