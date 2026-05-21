import yfinance as yf
import pandas as pd

ticker = "AAPL"

data = yf.download(
    ticker,
    start="2019-01-01",
    end="2025-01-01"
)

# Remove multi-index columns if they exist
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Save clean CSV
data.to_csv("data/aapl.csv")

print(data.head())
print("CSV fixed and saved")