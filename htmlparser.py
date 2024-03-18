"""
Author: Lingyu Zhou (https://zhoulinyu.net)
Date: Mar 16, 2024
License: PRIVATE USE ONLY!
"""
from bs4 import BeautifulSoup
import csv
import re
import os
import requests

def html2csv (url,outputpath="./1.csv"):
    soup=BeautifulSoup(requests.get(url).text)
    hotels_data = ""
    for hotel_section in soup.find_all('div', class_='info'):
        hotel_name = hotel_section.find("h3",class_="title").text.strip().split("\n")[0]
        star_level = hotel_section.find("h3",class_="title").text.strip().split("\n")[1].strip("[]")
        address = hotel_section.find("span",class_="street").text.strip()
        region = hotel_section.find("span",class_="region").text.strip()
        try:
            space=re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item meetingroom_space_range').text.strip().split("：")[1])
        except Exception:space="NaN"
        
        try:
            max_occupancy = re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item meetingroom_max_people_num').text.strip().split("：")[1])

        except Exception:max_occupancy="NaN"

        try:
            meeting_venue_number = re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item').text.strip().split("：")[1])

        except Exception:meeting_venue_number="NaN"

        try:
            hotel_room_number = re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item guestroom_total_num').text.strip().split("：")[1])

        except Exception:hotel_room_number="NaN"

        try:
            venue_price = re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item meetingroom_reference_price').text.strip().split("：")[1])

        except Exception:venue_price="NaN"

        try:
            hotel_price = re.sub("[起￥间㎡人,]", "",hotel_section.find('span', class_='info-base-item guestroom_reference_price').text.strip().split("：")[1])
        except Exception:hotel_price="NaN"

        hotels_data+=(",".join([hotel_name, star_level, address, region, space, max_occupancy, meeting_venue_number, hotel_room_number, venue_price, hotel_price]))
        hotels_data+="\n"

    file_exists = os.path.isfile(outputpath)
    need_newline = file_exists and os.path.getsize(outputpath) > 0

    with open(outputpath, 'a' if file_exists else 'w', newline='', encoding='utf-8') as txt:
        # if not file_exists:
        #     txt.write(",".join(['Hotel Name', 'Star Level', 'Address', 'Region', 'Area', 'Max Occupancy', 'Meeting Venue Number', 'Hotel Room Number', 'Venue Price(from)', 'Hotel Price\n']))
        txt.write(hotels_data)

    print('Data extraction writing completed.')
