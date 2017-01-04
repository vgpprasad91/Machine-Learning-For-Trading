
# write a function to read the empty dataframe
def test_run():
  
  # import pandas
  import pandas as pd
  
  # write a command to read in the date_range
  start_date = "2010-01-22"
  end_date = "2010-01-26"
  dates = pd.date_range(start_date, end_date)
  
  # create an empty dataframe with the date_range as the index
  df = pd.DataFrame(index=dates)
  
  # Read the SPY data into a temporary dataframe
  dfSPY = pd.read_csv("data/SPY.csv",index_col="Date",parse_dates=True, usecols=['Date','Adj Close'],na_values=['nan'])
  
  # Join the two dataframes using DataFrame.join()
  df = df.join(dfSPY,how="inner") # dataframe.join() does a left join by default
  
  # Join and drop na using the inner attribute of the how property 
  
  # Drop the rows where it is na
  #df = df.dropna()
  #print df

# write a command to read in the main funcion
int __name__ == "main":
  test_run()
