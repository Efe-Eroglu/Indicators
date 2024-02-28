import yfinance as yf
import matplotlib.pyplot as plt

ticker_info =input("Hisse İşlem Kodu/Share Transaction Code :")
ticker = yf.Ticker(ticker_info)

data = ticker.history(period="1y", interval="1d")

data["SMA"] = data["Close"].rolling(window=20).mean()

data["SD"] = data["Close"].rolling(window=20).std()

data["UB"] = data["SMA"] + (2*data["SD"])
data["LB"] = data["SMA"] - (2*data["SD"])

plt.figure(figsize=(10,6))

plt.plot(data.index, data["Close"], label="Fiyat", color="blue")

plt.fill_between(data.index, data["UB"], data["LB"], color="darkgreen", alpha=0.5, label="Bollinger Bandı")

plt.plot(data.index, data["UB"],label="Üst Bollinger Bandı", color="#FF2323")  
plt.plot(data.index, data["LB"], label="Alt Bollinger Bandı",color="#006400")

plt.plot(data.index, data["SMA"], label="Orta Bollinger Bandı", color="#464646")

plt.title("Bollinger Bandı")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.legend()
plt.grid(True)

plt.savefig(f"{ticker_info}.png")
plt.show()


