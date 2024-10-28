import pandas as pd
#........(1)..........
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X': [65, 55, 74, 80, 82, 79, 75, 75, 80, 76],
    'Y': [61, 50, 80, 82, 81, 74, 77, 82, 79, 80]
    }
df = pd.DataFrame(data)
print(df.head())
print("Mean: ", df[['X','Y']].mean())
print("Standard deviation: ", df[['X', 'Y']].std())
df.plot.scatter(x='X', y='Y')
print(df[['X', 'Y']].corr())


