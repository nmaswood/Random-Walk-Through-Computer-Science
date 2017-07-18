import pandas as pd

df = pd.DataFrame({
    'random': [1234,4567,902],
   'year_month': ['2013-12-01', '2016-12-01','2012-12-01']
})

def filter_data(df, start, end):

    """
    Takes df

    * Sorts it
    * Removes dates in the range (start, end) specified
    * Returns new df

    This function does not modify the original data but creates a new data frame.

    """

    df2 = df.copy()
    df2 = df2.sort_values('year_month')
    df2['year_month'] = pd.to_datetime(df['year_month'])
    df2 = df2[(df2['year_month'] < end) & (df2['year_month'] > start)]

    return df2

new_df = filter_data(df,'2013-11-01', '2017-12-01' )

print (new_df)