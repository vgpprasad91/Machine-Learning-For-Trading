# write a function to get the mean volume
def get_mean_volume(symbol):
  
  # import pandas
  import pandas as pd
  
  # write a command to get the data into a dataframe
  df = pd.read_csv('data/{}.csv'.format(symbol))
  
  # return the mean volume of the stocks
  return df['Volume'].mean()

# write a function to pass the symbols for finding the mean
def test_run():
  for symbol in ['AAPL','Goog']:
    print 'mean volume:'
    print symbol, get_mean_volume(symbol)


# write a main command to run standalone

int __name__ == "main":
  test_run()
