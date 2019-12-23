from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
import time
from datetime import datetime,date,timedelta
# from dateutil.relativedelta import relativedelta

today = datetime.today()
count = 0
base_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/numbers/numbers4/index.html?year={0}&month={1}'

while True:

    maeMonth = 11
    # year = datetime.strftime(maeMonth, '%Y')
    # month = datetime.strftime(maeMonth, '%m')
    year = 2019
    month = 11

    url = base_url.format(year,month)
    # print(url)
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    browser.quit()

    soup = BeautifulSoup(html)
    tables = soup.findAll(attrs={"class": "typeTK"})

    print(soup)
    print(tables)
    
    for table in tables:
        trs = table.findAll('tr')
        kai = trs[0].findAll('th')[1].text
        hi = trs[1].find('td').text
        hit = trs[2].find('td').find('strong').text
        st = trs[3].findAll('td')[0].text
        st_price = trs[3].findAll('td')[1].find('strong').text
        box = trs[4].findAll('td')[0].text
        box_price = trs[4].findAll('td')[1].find('strong').text
        set_st = trs[5].findAll('td')[0].text
        set_st_price = trs[5].findAll('td')[1].find('strong').text
        set_box = trs[6].findAll('td')[0].text
        set_box_price = trs[6].findAll('td')[1].find('strong').text
        #mini = trs[7].findAll('td')[0].text
        #mini_price = trs[7].findAll('td')[1].find('strong').text
        allprice = trs[7].find('td').text
        print(kai, hi , hit, st, st_price, box, box_price, set_st, set_st_price, set_box,set_box_price, allprice)

    # try:
        
    #     browser = webdriver.Firefox()
    #     browser.get(url)
    #     time.sleep(2)
    #     html = browser.page_source
    #     browser.quit()

    #     soup = BeautifulSoup(html)
    #     tables = soup.findAll(attrs={"class": "typeTK"})

    #     print(soup)
        
    #     for table in tables:
    #         trs = table.findAll('tr')
    #         kai = trs[0].findAll('th')[1].text
    #         hi = trs[1].find('td').text
    #         hit = trs[2].find('td').find('strong').text
    #         st = trs[3].findAll('td')[0].text
    #         st_price = trs[3].findAll('td')[1].find('strong').text
    #         box = trs[4].findAll('td')[0].text
    #         box_price = trs[4].findAll('td')[1].find('strong').text
    #         set_st = trs[5].findAll('td')[0].text
    #         set_st_price = trs[5].findAll('td')[1].find('strong').text
    #         set_box = trs[6].findAll('td')[0].text
    #         set_box_price = trs[6].findAll('td')[1].find('strong').text
    #         #mini = trs[7].findAll('td')[0].text
    #         #mini_price = trs[7].findAll('td')[1].find('strong').text
    #         allprice = trs[7].find('td').text
    #         print(kai, hi , hit, st, st_price, box, box_price, set_st, set_st_price, set_box,set_box_price, allprice)
        
    #     count = count + 1
    #     if count > 1:
    #         break
            
    # except:
    #     print('error')
    # finally:
    #     try:
    #         browser.quit()
    #         pass
    #     except:
    #         pass