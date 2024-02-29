import mplfinance as mpf
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt


start_time = dt.datetime(2023,1,1)
end_time = dt.datetime.now()

ticker = input("Hisse işlem kodu : ")

option = int(input("-- Renklendirme Tercihi -- \nVarsayılan / Özel (0/1) : "))

if option == 1:

    for index,i in enumerate(mpf.available_styles()):
        print(f"{index}-) {i}")

    style = input("Hangi stili kullanmak istersiniz : ")

    up = input("Yükseliş mum rengi : ") 
    down = input("Düşüş mum rengi : ") 
    wick = input("İğne rengi : ") 
    edge = input("Kenar rengi : ") 

    colors = mpf.make_marketcolors(up=up, down=down, wick=wick,edge=edge)

    mpf_style = mpf.make_mpf_style(base_mpf_style=mpf.available_styles()[int(style)], marketcolors=colors)


elif option == 0:
    
    colors = mpf.make_marketcolors(up="green",down="red",wick="inherit",edge="inherit")

    mpf_style = mpf.make_mpf_style(base_mpf_style="binance", marketcolors=colors)

else:
    print("Geçerli bir seçenek girin.")
    exit()

data = yf.download(ticker, start=start_time, end=end_time)

mpf.plot(data, type="candle", style=mpf_style,figscale=1.5)

plt.savefig(f"{ticker}.png")