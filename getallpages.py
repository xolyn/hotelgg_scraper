"""
Author: Lingyu Zhou (https://zhoulinyu.net)
Date: Mar 16, 2024
License: PRIVATE USE ONLY!
"""
import requests
from bs4 import BeautifulSoup

def getpager(starturl):
    allurl=[]
    response = requests.get(starturl)
    if response.status_code == 200:
        soup=BeautifulSoup(requests.get(starturl).text)
        pagerstr =str(soup.find('div',class_="pager"))
        pager = BeautifulSoup(pagerstr, 'html.parser')
        a_tags = pager.find_all('a')
        allurl.extend([[tag.text.strip(),tag.get('href')]  for tag in a_tags if tag.text.strip() not in ["下一页","上一页"] ])
        for idx in range(len(allurl)):
            if allurl[idx]=="...":
                allurl.pop(idx) 
                break
    else:
        print(f"Failed to retrieve the webpage: Status code {response.status_code}")
    return allurl