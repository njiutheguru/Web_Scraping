import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Simple stock Price App
Shown are the stock closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id',start='2010-5-31', end='2020-5-31')
                                   # Open high and low close volume Dividends stock splits
st.write("""
### Closing Price
         """)
st.line_chart(tickerDf.Close)
st.write("""
### Volume Quantity
         """)
st.line_chart(tickerDf.Volume)
                                 