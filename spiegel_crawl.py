# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:21:52 2021

@author: z0040scd
"""

import requests
from bs4 import BeautifulSoup

schlagzeilen_url = "https://www.spiegel.de/schlagzeilen/"
r = requests.get(schlagzeilen_url)
html_code = r.text

doc = BeautifulSoup(html_code, 'html.parser')

main = doc.find('main', id='Inhalt')
headlines = main.find_all('a', attrs={'title' : True})
datumsangaben = doc.find_all(attrs = {'class' : 'font-sansUI text-shade-dark text-s mt-4'})
info = doc.find_all(attrs = {'class' : 'font-sansUI text-shade-dark text-s mt-4'})

with open(r"C:\Users\z0040scd\Documents\SPIEGEL.txt", "w", encoding="utf-8") as file:
    for infos, datum, headline in zip(info, datumsangaben, headlines):
        amade = requests.get(headline['href'])
        ljulia = amade.text
        toffifee = BeautifulSoup(ljulia, 'html.parser')
        datetime = toffifee.find('time')
        datetime_string = ''
        if datetime is None:
            datetime_string = '00:00'
        else:
            datetime_string = datetime['datetime']
        
        file.write(infos.span.next_sibling.next_sibling.next_sibling.next_sibling.text + ",")
        file.write(datetime_string + ",")
        file.write(headline['title'] + "\n")

        
    





        

        
        
