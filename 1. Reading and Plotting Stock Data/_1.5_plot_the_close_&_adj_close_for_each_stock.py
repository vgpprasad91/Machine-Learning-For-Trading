
# write a code to plot the close and adj close columns
def plot_close_adj_close(symbol):
  
  # import pandas
  import pandas as pd
  
  # import matplotlib
  import matplotlib.pyplot as plt
  
  # write a code to read the data into the dataframe
  df = pd.read_csv('data/{}.csv'.format(symbol))
  
  # write code to plot close and adj close columns for each symbol
  df[['close','Adj Close']].plot()
  plt.show()

# write a code to get each symbol from stocks list
def test_run():
  for symbol in ['AAPL','Goog']:
    plot_close_adj_close(symbol)

# write a code to activate the main function
int __name__ == "main":
  test_run()
