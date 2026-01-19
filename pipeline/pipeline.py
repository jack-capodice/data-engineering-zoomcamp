import sys
import pandas as pd

# Arguments
print('arguments', sys.argv)

month = int(sys.argv[1])
print(f"Hello, pipeline! Month: {month}")

# Pandas
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_month_{month}.parquet")