"""
Author: Lingyu Zhou (https://zhoulinyu.net)
Date: Mar 16, 2024
License: PRIVATE USE ONLY!
"""
import getallpages
import htmlparser

url=input("Enter the first page")

allurl=getallpages.getpager(url)


# while True:
for _ in range(11):
    # urls=allurl[:]
    thisurl=allurl[-1][1]
    moreurl=getallpages.getpager(thisurl)
    # print(moreurl)
    allurl.extend(moreurl)

hotelurl=[]
for i in range(len(allurl)):
    if allurl[i][0]!="..." and allurl[i] not in hotelurl:
        hotelurl.append(allurl[i])


for itm in hotelurl:
    htmlparser.html2csv(itm[1])
    print(round(int(itm[0])*100/101 ,2),"％ completed",sep="")