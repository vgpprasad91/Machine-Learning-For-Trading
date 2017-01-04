# write a function to get the max close for each of the stocks

def get_max_close(symbol):
  
  # import pandas library
  import pandas as pd
  
  # data for each stock is stored in a file: data/<symbol>.csv
  # get the stock data in a dataframe
  df = pd.read_csv('data/{}.csv'.format(symbol)
  
  # return the max close for each stock data
  return df['Close'].max()

# write a test run function to pass the symbols to the get max function

def test_run():
  for symbol in ['Goog','AAPL']:
    print 'Max Close: '
    print symbol, str(get_max_close(symbol))

# write the main function for the standalone run

int __name__ == "main":
  test_run()
