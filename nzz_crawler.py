# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:43:25 2021

@author: Julia
"""

from bs4 import BeautifulSoup
import requests

my_url = 'https://www.nzz.ch'
r = requests.get(my_url)
soup = BeautifulSoup(r.content, 'html.parser')

category = soup.find_all('a', class_='mainmenu__link')

for pflanze in category:
    r2 = requests.get(my_url + pflanze["href"])
    soupy = BeautifulSoup(r2.content, 'html.parser')

    date = soup.find_all('time', class_='metainfo__item metainfo__item--date')
    title = soup.find_all('span', class_='teaser__title-name')

    with open(r"C:\Users\Julia\Documents\nzz.txt", "a", encoding="utf-8") as file:
        for date2, title2 in zip(date, title):
            feli = date2["datetime"].replace("T", " ").split(".")
            amasee = title2.text.replace("\n", "")
        
            file.write(pflanze.text + ",")
            file.write(feli[0] + ",")
            file.write(amasee + "\n")
