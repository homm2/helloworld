import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title('H&P stock price')
Stock_Symbol = 'HP'
StockData = yf.Ticker(Stock_Symbol)
StockChart = StockData.history(period = '1d', start='2022-01-01', end='2022-12-31')
st.line_chart(StockChart.Close)
st.line_chart(StockChart.Volume) # Open High Low Close Volume Dividens Stock Spline


