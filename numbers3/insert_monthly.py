
from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime
import time
import csv

# 指定
MONTH = '201912'
URL = 'https://takarakuji.rakuten.co.jp/backnumber/numbers3/201912/'
CSV_FILE = '../assets/numbers3/201912.csv'

# アウトプット情報
output = open(CSV_FILE, mode='w')

# スクレイピング
scraping = BeautifulSoup(requests.get(URL).content,'html.parser')

# HTMLタグ
tag_table = scraping.find_all('table')
# 月間当選番号など
# テーブル各データ取得
data = []
for _i in range(1, len(tag_table)):
    info = [d.text for d in tag_table[_i].find_all('td')]
    data.append(info)

# CSVへ挿入
for _j in data:
    writer = csv.writer(output)
    writer.writerow(_j)

print('end')