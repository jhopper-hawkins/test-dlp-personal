"""
apple_bollinger_demo.py

Demo script for Cyberhaven POVs.
It retrieves Apple stock data using yfinance and computes Bollinger Bands.

✅ Safe to run — uses public data (no secrets or credentials required)
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Pull Apple stock data ---
ticker = "AAPL"
data = yf.download(ticker, start="2024-01-01", end="2025-01-01")

# --- Step 2: Calculate Bollinger Bands ---
# 20-day simple moving average (SMA)
data["SMA_20"] = data["Close"].rolling(window=20).mean()

# Standard deviation for the same period
data["STDDEV"] = data["Close"].rolling(window=20).std()

# Upper and lower Bollinger Bands
data["Upper_Band"] = data["SMA_20"] + (data["STDDEV"] * 2)
data["Lower_Band"] = data["SMA_20"] - (data["STDDEV"] * 2)

# --- Step 3: Print summary ---
print("✅ Pulled Apple stock data")
print(data.tail(5)[["Close", "SMA_20", "Upper_Band", "Lower_Band"]])

# --- Step 4: Plot the Bollinger Bands ---
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Close"], label="AAPL Close", linewidth=1)
plt.plot(data.index, data["SMA_20"], label="20-Day SMA", linewidth=1)
plt.plot(data.index, data["Upper_Band"], label="Upper Band", linestyle="--", linewidth=1)
plt.plot(data.index, data["Lower_Band"], label="Lower Band", linestyle="--", linewidth=1)

plt.title("Apple (AAPL) - Bollinger Bands")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
