import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

ticker=input("Hisse İşlem Kodu/Share Transaction Code :")

start_time = dt.datetime(dt.datetime.now().year - 1, 1, 1)
end_time = dt.datetime.now()

data = yf.download(ticker, start=start_time, end=end_time)

high9 = data.High.rolling(9).max()
low9 = data.High.rolling(9).min()

high26 = data.High.rolling(26).max()
low26 = data.High.rolling(26).min()

high52 = data.High.rolling(52).max()
low52 = data.High.rolling(52).min()

data["tenkan_sen"] = (high9 + low9) / 2
data["kijun_sen"] = (high26 + low26) / 2
data["senkou_A"] = ((data.tenkan_sen + data.kijun_sen) / 2).shift(26)
data["senkou_B"] = ((high52 + low52) / 2).shift(26)
data["chikou"] = data.Close.shift(-26)
data = data.iloc[26:]


fig, ax = plt.subplots(figsize=(16, 9)) 
plt.plot(data.index, data["tenkan_sen"], lw=0.8)
plt.plot(data.index, data["kijun_sen"], lw=0.8)
plt.plot(data.index, data["chikou"], lw=0.8)
plt.title("Ichimoku: " + str(ticker))
plt.ylabel("Fiyat")

plt.plot(data.index, data["Adj Close"], lw=1.3, color="b")

plt.fill_between(data.index, data.senkou_A, data.senkou_B, where=data.senkou_A >= data.senkou_B, color="lightgreen")
plt.fill_between(data.index, data.senkou_A, data.senkou_B, where=data.senkou_A < data.senkou_B, color="lightcoral")

plt.grid()
plt.savefig(f"{ticker}.png")
plt.show()
