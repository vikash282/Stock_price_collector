from fetch_prices import fetch_stock_prices
from fetch_news import fetch_finance_news

def run_pipeline():
    print(" Starting Finance Data Pipeline...\n")
    fetch_stock_prices("TSLA")   # Fetch Tesla stock prices
    fetch_finance_news()         # Fetch business news
    print("\n Pipeline execution finished.")

if __name__ == "__main__":
    run_pipeline()
