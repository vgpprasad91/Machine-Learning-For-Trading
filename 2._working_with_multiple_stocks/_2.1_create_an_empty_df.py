
# write a function to create an empty dataframe
def test_run():
  
  # import pandas
  import pandas as pd
  
  # create a date_range
  start_date = "2010-01-22"
  end_date = "2010-01-26"
  dates = pd.date_range(start_date,end_date)
  
  # Create an empty dataframe with the date range as the index
  df1 = pd.DataFrame(index=dates)

# write a main command
int __name__ == "main":
  test_run()
