import backtrader as bt
import pandas as pd

from strategies.ma_crossover import MovingAverageCrossStrategy

# Create cerebro engine
cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(MovingAverageCrossStrategy)

# Load CSV
df = pd.read_csv(
    "data/aapl.csv",
    parse_dates=True,
    index_col=0
)

# Convert to Backtrader feed
data = bt.feeds.PandasData(dataname=df)

# Add data
cerebro.adddata(data)

# Broker settings
cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.001)

# Add analyzers
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')

print("Starting Portfolio Value:", cerebro.broker.getvalue())

# Run backtest
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
results = results = cerebro.run()

strat = results[0]

print("Return:",
      strat.analyzers.returns.get_analysis())

print("Drawdown:",
      strat.analyzers.drawdown.get_analysis())

strat = results[0]

print("Final Portfolio Value:", cerebro.broker.getvalue())

print("Returns:")
print(strat.analyzers.returns.get_analysis())

print("Drawdown:")
print(strat.analyzers.drawdown.get_analysis())

# Plot
cerebro.plot()