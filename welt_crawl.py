# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:49:14 2021

@author: z0041r3p
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://gadgets.ndtv.com/news")
soup = BeautifulSoup(page.content, 'html.parser')

def find_news_articles():
    all_news_articles = []
    all_spans = soup.findAll('span',{'class':'news_listing'})
    for span in all_spans:
        all_news_articles.append(span.get_text())
    return all_news_articles

def find_authors_and_dates():
    all_authors_and_dates = []
    all_divs = soup.findAll('div',{'class':'dateline'})
    for div in all_divs:
        all_authors_and_dates.append(div.get_text())
    return all_authors_and_dates

def format_output():
    output_lines = []
    news_articles = find_news_articles()
    authors_and_dates = find_authors_and_dates()
    for i in range(len(news_articles)):
        output = news_articles[i] + ' - ' + authors_and_dates[i] + '\n'
        output_lines.append(output)
    return output_lines

def save_to_file():
    output = format_output()
    with open("C:/TEST/data.txt", "w") as file:
        file.writelines(output)
        file.close()
        print("file created successfully")

save_to_file()