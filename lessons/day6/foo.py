"""
>>> import datetime
>>> dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
>>> dates.sort()
>>> sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
>>> sorteddates
['2010-01-12', '2010-01-14', '2010-02-07', '2010-02-11', '2010-11-16', '2010-11-
22', '2010-11-23', '2010-11-26', '2010-12-02', '2010-12-13', '2011-02-04', '2011
-06-02', '2011-08-05', '2011-11-30']
"""

import pandas as pd


df = pd.DataFrame(
    {'fuck': [0,1,2],
   'year_month': ['2016-12-01', '2016-12-02','2016-12-03']})

def filter_data(df, start, end):

    """
    This function takes a data frame and returns a one where
    the column year_month only has dates in between the range
    of start and end

    This function does not modify the original data but creates a new data frame.


    """

    df2 = df.copy()
    df2['year_month'] = pd.to_datetime(df['year_month'])
    df2 = df2[(df2['year_month'] < end) & (df2['year_month'] > start)]

    return df2

new_df = filter_data(df,'2016-12-01', '2016-12-03' )

print (new_df)