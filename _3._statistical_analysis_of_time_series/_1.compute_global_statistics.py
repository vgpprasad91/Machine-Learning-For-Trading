

# write a test run function to get the symbols
def test_run():
  # Read data
  dates = pd.date_range("2010-01-01","2012-12-31")
  symbols = ["Goog", "SPY", "XOM", "GLD"]
  df = get_data(symbols, dates)
  plot_data(df)
  
  # Compute global statistics
  print df.mean()
  print df.median()
  print df.std()

# write a int main function to pass the main function
int __name__ == "main":
  test_run()
