import datetime as dt
import yfinance as yf
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


ticker=input("Hisse İşlem Kodu/Share Transaction Code :")
ticker_info = yf.Ticker(ticker)


start_time = dt.datetime(dt.datetime.now().year-1, 1, 1)
end_time = dt.datetime.now()


data = yf.download(ticker, start=start_time, end=end_time)


def SMA(data, period = 30, column='Close'):
    return data[column].rolling(window=period).mean()

data['SMA20']=SMA(data, 20)
data['SMA50']=SMA(data, 50)

data['Signal'] = np.where(data['SMA20'] > data['SMA50'], 1, 0)
data['Position'] = data['Signal'].diff()

data['Buy'] = np.where(data['Position'] == 1, data['Close'], np.NAN)
data['Sell'] = np.where(data['Position'] == -1, data['Close'], np.NAN)


plt.figure(figsize =(16,8))
plt.title('Kapanış Fiyat Geçmişi | Alış & Satış Sinyali', fontsize = 18)
plt.plot(data['Close'], alpha = 0.5, label='Close')
plt.plot(data['SMA20'], alpha = 0.5, label='SMA20')
plt.plot(data['SMA50'], alpha = 0.5, label='SMA50')
plt.scatter(data.index, data['Buy'], alpha = 1, label='Alış Sinyali', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell'], alpha = 1, label='Satış Sinyali', marker = 'v', color = 'red')
plt.xlabel('Tarih', fontsize=18)
plt.ylabel('Kapanış Fiyatı', fontsize=18)

plt.savefig(f"{ticker}.png")
plt.show()