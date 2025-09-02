import yfinance as yf
from config import get_mongo_connection

def fetch_stock_prices(ticker="TSLA"):
    print(f"Fetching stock data for {ticker}...")

    data = yf.download(ticker, period="5d", interval="1d")
    if data.empty:
        print("No stock data fetched.")
        return

    db = get_mongo_connection()
    if db is None:
        return


    collection = db["stock_prices"]

    for date, row in data.iterrows():
        doc = {
            "ticker": ticker,
            "date": str(date.date()),
            "open": float(row["Open"].iloc[0] if hasattr(row["Open"], "iloc") else row["Open"]),
            "close": float(row["Close"].iloc[0] if hasattr(row["Close"], "iloc") else row["Close"]),
            "volume": int(row["Volume"].iloc[0] if hasattr(row["Volume"], "iloc") else row["Volume"])
        }
        collection.update_one(
            {"ticker": ticker, "date": doc["date"]},
            {"$set": doc},
            upsert=True
        )
    print(f" {ticker} stock data inserted/updated.")
