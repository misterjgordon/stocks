import pandas as pd
import numpy as np
import yfinance as yf
import yahoo_fin.stock_info as si
import yahoo_fin.news as news
import datetime as dt
from datetime import timedelta
from tzlocal import get_localzone
from pandas_datareader import data as pdr

# TODO install formatter

# yf.pdr_override()



def temp():
    start = dt.datetime.now() - dt.timedelta(days=3)
    end = dt.datetime.now()

    sp500 = si.tickers_sp500()  # get lsit of all tickers in sp500

    prices = {}  # create empty dictionary to store the prices data
    for ticker in sp500:
        prices[ticker] = si.get_data(ticker, start, end)

        print(prices)
def temp():
    start = dt.datetime.now() - dt.timedelta(days=3)
    end = dt.datetime.now()

    sp500 = si.tickers_sp500()  # get lsit of all tickers in sp500

    prices = {}  # create empty dictionary to store the prices data
    for ticker in sp500:
        prices[ticker] = si.get_data(ticker, start, end)

        print(prices)
def temp():
    start = dt.datetime.now() - dt.timedelta(days=3)
    end = dt.datetime.now()

    sp500 = si.tickers_sp500()  # get lsit of all tickers in sp500

    prices = {}  # create empty dictionary to store the prices data
    for ticker in sp500:
        prices[ticker] = si.get_data(ticker, start, end)

        print(prices)
