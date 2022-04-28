# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:28:03 2022

Web Scraping - get data from finviz and output to a file with Dictionary Writer
@author: tomfoolc
"""

import requests
from bs4 import BeautifulSoup
import csv

# Start - define function
"""
def getTicker():
    return input('Enter a ticker: ')
"""
    
def getFinvizTickerUrl(_ticker):
    return "https://finviz.com/quote.ashx?t="+_ticker.strip().lower()

def getFinvizTickerPage(_url):
    try:
        _headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        _response = requests.get(_url, headers=_headers)
        return BeautifulSoup(_response.text, "html.parser")

    except Exception as e:
        return e
    
def getTickerPerfReturn(_ticker,_soup): 
    try:
        _valueReturn = {"Ticker":ticker.upper()}

        _tables = _soup.select('table.snapshot-table2')
        _table_rows = _tables[0].findAll('tr')

        for _table_row in _table_rows:
            _table_tds = _table_row.findAll('td')
            for _table_td in _table_tds:
                if (_table_td.text == "Perf Month"):
                    _next_node = _table_td.find_next_siblings("td")
                    _valueReturn.update({"Month Return":float((_next_node[0].text).replace("%",""))})
                if (_table_td.text == "Perf Quarter"):
                    _next_node = _table_td.find_next_siblings("td")
                    _valueReturn.update({"Quarter Return":float((_next_node[0].text).replace("%",""))})
                if (_table_td.text == "Perf Half Y"):
                    _next_node = _table_td.find_next_siblings("td")
                    _valueReturn.update({"Half Year Return":float((_next_node[0].text).replace("%",""))})
                if (_table_td.text == "Perf Year"):
                    _next_node = _table_td.find_next_siblings("td")
                    _valueReturn.update({"Year Return":float((_next_node[0].text).replace("%",""))})

        return _valueReturn
    except Exception as e:
        return e
# End - define function

tickerList = ["SPY","ACWX","AGG"]
data = []
for ticker in tickerList:
    url = getFinvizTickerUrl(ticker)
    soup = getFinvizTickerPage(url)
    data.append(getTickerPerfReturn(ticker,soup))

header = ["Ticker","Month Return","Quarter Return","Half Year Return","Year Return"]

#use "with open" to open the file, no need to close file
with open("./adm.csv","w",encoding="UTF8",newline="") as f:
          #writer = csv.writer(f)
          #change to use Dictonary Writer
          writer = csv.DictWriter(f, fieldnames=header)
          
          #write the header
          #writer.writerow(header)
          writer.writeheader()
          
          #write multiple data
          writer.writerows(data)
