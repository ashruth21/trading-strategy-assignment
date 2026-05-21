import pandas as pd

data = pd.read_csv("data/aapl.csv")

windows = []

train_size = 500
test_size = 100

start = 0

while start + train_size + test_size < len(data):

    train = data[start:start+train_size]

    test = data[start+train_size:start+train_size+test_size]

    windows.append((train, test))

    start += test_size

print("Total Walk Forward Windows:", len(windows))