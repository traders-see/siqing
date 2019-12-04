'''
什么是API ： Appliscation Programming Interface
'''
import requests
import pandas as pd
import time
pd.set_option('expand_frame_repr', False)  # 显示列都看见
pd.set_option('display.max_rows', 1000)
#  url K  kline data线
url = 'https://api.huobi.pro/market/history/kline?period=60min&size=400&symbol=btcusdt'
print(url)
resp = requests.get(url)
print(resp)
r_json = resp.json()
print(r_json)
data = r_json['data']
print(data)
df = pd.DataFrame(data)
print(df)
#  获取ticker 数据，盘口数据
while True:
    ticker_url =  "https://api.huobi.pro/market/detail/merged?symbol=btcusdt"
    ticker_1 = requests.get(ticker_url)
    ticker_2 = ticker_1.json()
    print(ticker_2)
    ticker_2 = ticker_2['tick']
    print(ticker_2)
    df1 = pd.DataFrame(ticker_2)
    print(df1)
    time.sleep(1)
    break

