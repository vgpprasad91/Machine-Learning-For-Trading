# To read the contents of a CSV file into Pandas

import pandas as pd

df = pd.read_csv('input_file.csv')

# Select the first 5 rows from a dataframe

df.head(n=5)

# Select the last 5 rows from a dataframe

df.tail(n=5)
