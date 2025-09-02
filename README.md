# 📈 Stock Price & News Collector

A simple **finance data pipeline** that fetches stock prices and finance-related news headlines, then stores them into a **MongoDB** database.  
This project is built using Python, `yfinance`, `pymongo`, and `requests`.

---

## 🚀 Features
- Fetches **latest stock prices** (Open, Close, Volume, etc.) using [Yahoo Finance](https://pypi.org/project/yfinance/).
- Collects **latest finance news headlines** from a news API.
- Stores all data into **MongoDB** for later analysis.
- Designed as a **modular pipeline** for easy extension.

---

## 🛠 Project Structure
finance/
│── Data_pipeline.py # Main pipeline runner
│── fetch_prices.py # Fetches stock prices from Yahoo Finance
│── fetch_news.py # Fetches finance news headlines
│── db.py # MongoDB connection helper
│── config.py # Config (DB URI, API keys, etc.)
│── requirements.txt # Python dependencies

---
📊 Example Data in MongoDB

Stock Data Collection (stock_prices):

{
  "ticker": "TSLA",
  "date": "2025-09-02",
  "open": 245.67,
  "close": 248.12,
  "volume": 12345678
}


News Data Collection (news):

{
  "headline": "Tesla stock rises after new model announcement",
  "source": "Yahoo Finance",
  "date": "2025-09-02"
}
