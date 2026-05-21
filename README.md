# Algorithmic Trading Strategy Assignment

## Project Overview

This project implements an algorithmic trading strategy using Python and Backtrader.

The strategy uses a Moving Average Crossover system:

- Buy when the short-term moving average crosses above the long-term moving average
- Sell when the short-term moving average crosses below the long-term moving average

The project also includes:

- Historical data download using yfinance
- Backtesting using Backtrader
- Walk-Forward Analysis
- Robustness Score calculation

---

# Strategy Logic

## Entry Rule

Buy when:

- 20-day Moving Average crosses above 50-day Moving Average

## Exit Rule

Sell when:

- 20-day Moving Average crosses below 50-day Moving Average

## Risk Management

- Fixed starting capital
- Commission included
- Strategy tested across multiple periods

---

# Project Structure

```text
trading-strategy-assignment/
│
├── data/
│   ├── aapl.csv
│   └── download_data.py
│
├── strategies/
│   └── ma_crossover.py
│
├── results/
│
├── main.py
├── walk_forward.py
├── robustness.py
├── requirements.txt
└── README.md