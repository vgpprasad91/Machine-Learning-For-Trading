# To read the contents of a CSV file into Pandas

import pandas as pd

def test_run():
  df = pd.read_csv('input_file.csv')
  
  # Select the first 5 rows from a dataframe
  print df.head(n=5)
  
  # Select the last 5 rows from a dataframe
  print df.tail(n=5)
  
  # Slicing the dataframe
  print df[5:11] # rows between index 5 and 10

if __name__ == "main":
  test_run()
