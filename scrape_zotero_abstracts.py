'''
 # @ File Name: scrape_zotero_abstracts
 # @ Author: Alexander Karl
 # @ Create Time: 2025-01-13
 # @ Description: Scrape Abstracts and 
 '''

# 0. Overhead

import os
from bs4 import BeautifulSoup

zotero_url = "zotero_report_llm_articles.htm"

# 1. Cook that soup
zotero_soup = soup = BeautifulSoup(open(zotero_url, encoding="utf8"), "html.parser")
zotero_soup