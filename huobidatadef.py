import pandas as pd
import requests
import time
import os
import json
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)
# 异常抓取数据函数
def get_url_content(url, max_try_number):
    try_num = 0
    while True:
        try:
            return requests.get(url,timeout=10).json()
        except Exception as http_err:
            print(url, '抓取报错', http_err)
            try_num +=1
            if try_num >= max_try_number:
                print('尝试次数超过了')
                return None
# HB获取k线数据函数
hb_url = "https://api.huobi.pro"
k_url = "/market/history/kline?"
def get_k_hb(symbol_list=['btcusdt', 'eosusdt']):
    df = pd.DataFrame()
    for symbol in symbol_list:
        canshu_url = "period=1week&size=200&symbol=%s" % symbol
        hb_url1 = hb_url + k_url + canshu_url
        print(hb_url1)
        content = get_url_content(hb_url1, 3)  # 用上面自己写的函数来读取数据
        print(content)

        if content is None:  # 当返回内容为空的时候，跳过本次循环
            continue
        data = content['data']
        _df = pd.DataFrame(data)
        print(_df)

get_k_hb(symbol_list=['btcusdt', 'eosusdt'])

