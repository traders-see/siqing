import pandas as pd
import requests
import time
import os
import json
import datetime
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
# 异常抓取数据函数(通用）
def get_url_content(url, max_try_number):
    try_num = 0
    while True:
        try:
            return requests.get(url, timeout=10).json()
        except Exception as http_err:
            print(url, '抓取报错', http_err)
            try_num +=1
            if try_num >= max_try_number:
                print('尝试次数超过了')
                return None
#  获取hb_ticker数据
def get_list_ticker_from_huobi(symbol_list=['btcusdt','ethusdt','eosusdt']):
    #  创建空的df
    df = pd.DataFrame()
    # 遍历每个symbol
    for symbol in symbol_list:
        # 构建url
        url = 'https://api.huobi.pro/market/detail/merged?symbol=%s' % symbol
        # 用自己写的通用函数抓取数据
        content = get_url_content(url, 3)
        # 当返回内容空时候跳过本次循环
        if content is None:
            continue
        # content数据转换dataframe
        _df = pd.DataFrame(content)
        #print(_df)
        _df = _df[['tick']].T
        #print(_df)
        # 就是在列里加一个symbol,然后把这次抓取的币种复制给他，数据看的更明白
        _df['symbol'] = symbol
        #print(symbol)
        #  合并数据到df中
        df = df.append(_df, ignore_index=True)
        #print(df)
        df = df[['id', 'bid', 'ask', 'amount', 'vol', 'symbol']]
        print(df)

# 获取k线数据（candle)
def get_k_from_hb(period='30min',size='200',symbol='btcusdt'):
    #构建URL
    url = 'https://api.huobi.pro/market/history/kline?period=%s&size=%s&symbol=%s' % (period, size, symbol)
    #print(url)
    #用自己写的通用函数抓取数据
    content = get_url_content(url,5)
    if content is None:  # 当返回内容为空的时候跳过本次循环
        return pd.DataFrame()
    #print(content)
    data = content['data']
    #print(data)
    df = pd.DataFrame(data, dtype='float')
    df = df[['id', 'open', 'close', 'low', 'high', 'amount', 'count', 'vol']]
    df_name = df.rename(columns={'id':'open_time'}) #错误 改名字在学习
    # 去掉重复的时间
    df_name.drop_duplicates(subset=['open_time'], inplace=True, keep='first')
    #print(df_name.dtypes)
    #print(df_name)
    df_name['open_time'] = pd.to_datetime(df_name['open_time'], unit='ms')
    print(df_name)








#执行两个函数（盘口）（K线）
#df2 = get_list_ticker_from_huobi(symbol_list=['btcusdt'])
df3 = get_k_from_hb(period='60min',size='200',symbol='btcusdt')