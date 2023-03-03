from bs4 import BeautifulSoup
import pandas as pd
import requests
import cloudscraper
import datetime as dt
import time

data_keys = [
    'pair_name', 
    'ti_buy', 
    'ti_sell', 
    'ma_buy', 
    'ma_sell', 
    'S1', 
    'S2', 
    'S3', 
    'pivot', 
    'R1', 
    'R2', 
    'R3',
    'percent_bullish', 
    'percent_bearish'
]

def get_data_object(text_list, pair_id, time_frame):
    data = {}
    data['pair_id'] = pair_id
    data['time_frame'] = time_frame
    data['updated'] = dt.datetime.utcnow()
    for item in text_list:
        temp_item = item.split("=")
        if len(temp_item) == 2 and temp_item[0] in data_keys:
            data[temp_item[0]] = temp_item[1]

    if 'pair_name' in data:
        data['pair_name'] = data['pair_name'].replace("/", "_")

    return data

def investing_com_fetch(pair_id, time_frame):

    s = cloudscraper.create_scraper()


    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    params = dict(
        action = 'get_studies',
        pair_ID = pair_id,
        time_frame = time_frame
    )

    response = s.get("https://www.investing.com/common/technical_studies/technical_studies_data.php", params=params, headers=headers)

    # print(response.content)
    # print(response.status_code)

    text = response.content.decode("utf-8")
    
    index_start = text.index("pair_name=")
    index_end = text.index("*;*quote_link")

    data_str = text[index_start:index_end]
    split_data_str = data_str.split("*;*")

    return get_data_object(split_data_str, pair_id, time_frame)

def investing_com():
    data = []
    for pair_id in range(1, 12):
        for time_frame in [3600, 86400]:
            print(pair_id, time_frame)
            data.append(investing_com_fetch(pair_id, time_frame))
            time.sleep(0.5)

    return pd.DataFrame.from_dict(data)
