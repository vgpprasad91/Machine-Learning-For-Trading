
def plot_adj_close(symbol):
  
  # import pandas
  import pandas as pd
  
  # import matplotlib to plot values
  import matplotlib.pyplot as plt
  
  # write a command to read the data in a dataframe
  df = pd.read_csv('data/{}.csv'.format(symbol))
  
  ## write a command to plot the adjusted close column
  df['Adj Close'].plot()
  plt.show()

# write a function to get all the symbols
def test_run():
  for symbol in ['AAPL','Goog']:
    plot_adj_close(symbol)

# write the main command to run the function
int __name__ == "main":
  test_run()
