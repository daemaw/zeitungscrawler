# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:21:49 2021

@author: z004366p
"""
import requests
import hashlib
from bs4 import BeautifulSoup

def get_da_soup(url):
    web_html = requests.get(url)
    return BeautifulSoup(web_html.content, 'html.parser')

def crawl_article(url):
    art_soup = get_da_soup(url)
    timetag = art_soup.find('time')
    if timetag is None:
        return '0000'
    datetime = timetag['datetime']
    return datetime

def crawl_category(cat):
    csv_string = ''
    category = cat['data-title']
    #print(category + ', ' + cat['href'] + '\n')
    cat_soup = get_da_soup(cat['href'])
    articles = cat_soup.find_all('a', class_='sz-teaser')
    for a in articles:
        title = a.find('h3', class_='sz-teaser__title').string
        is_paywall = 'False'
        if a.find('title', string='SZ Plus'):
            is_paywall = 'True'
        datetime = crawl_article(a['href'])
        file = open('sueddeutsche.csv', 'a', encoding='utf-8')
        csv_string += category + ',' + datetime + ',' + title + ',' + is_paywall + '\n'
        file.write(csv_string)
        file.close()
    
        
    
    

web_url = "https://sueddeutsche.de"

soup = get_da_soup(web_url)

nav = soup.find('ul', {'id' : 'header-departments'})
nav_el = nav.find_all('a', attrs={'data-title' : True})
#print(type(nav_el))
for a in nav_el:
    crawl_category(a)

