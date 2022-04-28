# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:28:03 2022

Web Scraping - sample of requests.get
@author: tomfoolc
"""

import requests
from bs4 import BeautifulSoup

ticker = "SPY"
url = "https://finviz.com/quote.ashx?t="+ticker.lower()
broswer_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


response = requests.get(url, headers=broswer_headers)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.title)
#print(soup.title.text)

"""
ticker_titles = soup.findAll('a')
for ticker_title in ticker_titles:
    print(ticker_title)
"""

"""
#<a href="quote.ashx?t=SPY&ty=c&ta=1&p=d" class="fullview-ticker" id="ticker">SPY</a>
ticker_titles = soup.findAll('a', attrs={"class":"fullview-ticker"})
for ticker_title in ticker_titles:
    print(ticker_title)
"""

ticker_titles = soup.select('a.tab-link')
for ticker_title in ticker_titles:
    print(f"Here is: {ticker_title}")
