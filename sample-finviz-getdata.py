# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:28:03 2022

Web Scraping - sample of get data from finviz
@author: tomfoolc
"""

import requests
from bs4 import BeautifulSoup

ticker = "SPY"

url = "https://finviz.com/quote.ashx?t="+ticker.lower()
broswer_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


response = requests.get(url, headers=broswer_headers)
soup = BeautifulSoup(response.text, "html.parser")

detail_tables = soup.select('table.snapshot-table2')

""" you can uncomment for check the result
for detail_table in detail_tables:
    print(f"{detail_table}")
"""

detail_table_rows = detail_tables[0].findAll('tr')

for detail_table_row in detail_table_rows:
    """ you can uncomment for check the result
    print(detail_table_row)
    """    
    detail_table_tds = detail_table_row.findAll('td')
    for detail_table_td in detail_table_tds:
        """ you can uncomment for check the result
        print(detail_table_td.text)
        """
        if (detail_table_td.text == "Perf Month"):
            next_node = detail_table_td.find_next_siblings("td")
            monthReturn = float((next_node[0].text).replace("%",""))
        if (detail_table_td.text == "Perf Quarter"):
            next_node = detail_table_td.find_next_siblings("td")
            quarterReturn = float((next_node[0].text).replace("%",""))
        if (detail_table_td.text == "Perf Half Y"):
            next_node = detail_table_td.find_next_siblings("td")
            halfYearReturn = float((next_node[0].text).replace("%",""))
        if (detail_table_td.text == "Perf Year"):
            next_node = detail_table_td.find_next_siblings("td")
            yearReturn = float((next_node[0].text).replace("%",""))

#print("Month Return: ", monthReturn, sep="")
#print("Month Return: "+str(monthReturn))
print(f"Month Return: {monthReturn}")
print(f"Quarter Return: {quarterReturn}")
print(f"Half Year Return: {halfYearReturn}")
print(f"Year Return: {yearReturn}")
print(f"Average Return: {(monthReturn+quarterReturn+halfYearReturn)/3}")

