import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from datetime import timedelta
from tzlocal import get_localzone
from pandas_datareader import data as pdr


def get_df():
    yf.pdr_override()

    stock = input('Enter a stock ticker:')  # stock
    print(stock)

    startyear = 2021  # start
    startmonth = 10
    startday = 19

    start = dt.datetime.today() - timedelta(days=7)  # (startyear,startmonth,startday)
    now = dt.datetime.today()  # now

    df = pdr.get_data_yahoo(stock, start, now)
    return df

# ma=7
# smaString="Sma_"+str(ma)
# df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
# print (df)

# df=df.iloc[ma:]
# print (df)
