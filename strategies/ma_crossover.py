import backtrader as bt

class MovingAverageCrossStrategy(bt.Strategy):

    params = (
        ('fast', 20),
        ('slow', 50),
    )

    def __init__(self):
        self.fast_ma = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=self.params.fast
        )

        self.slow_ma = bt.indicators.SimpleMovingAverage(
            self.data.close,
            period=self.params.slow
        )

        self.crossover = bt.indicators.CrossOver(
            self.fast_ma,
            self.slow_ma
        )

    def next(self):

        if not self.position:
            if self.crossover > 0:
                self.buy()

        elif self.crossover < 0:
            self.sell()