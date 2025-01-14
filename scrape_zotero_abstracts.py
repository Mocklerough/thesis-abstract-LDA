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

# print(zotero_soup)
"""
Path is: 
<body>
 <ul class="report combineChildItems"> # Article-level elements
  <li class="" id="">                #
   <table>
    <tbody>
     <tr>                              # html table
      <th>Abstract<th>              # table-header cell
      <td>"abstract contents"</td>  # table-data cell
     </tr>
</close elements>
"""
"""
- There are multiple <tr> with other article items
bs4 needs to find "<th>Abstract<th>" to pull it's <td> data cell within the same <tr>
- There are multiple "<li>", often 2-3 per article, but the one  containing the abstract always begins with <h2>"article title"</h2>. I wanted to grab the article title anyway, so I'll use that to navigate.
- Article titles aren't great unique identifiers. I'll grab the DOI too (same structure as abstract), but not all articles will have this. Grab now, count later.

HTML plan:
Grab all <li> elements containing <h2> element, save as list of <li>
Over each <li>, pull out
    - <h2>
    - <table><tbody>(<tr> containing <th>Abstract</th>)<td>
    - <table><tbody>(<tr> containing <th>DOI</th>)<td>
store each as a dict element, in a list-of-dicts, save and pass to LDA script.
"""

# grab the right li elements
li_elements = zotero_soup.find_all('li', lambda li: li and li.find('h2') is not None)
# check results
print(len(li_elements)) # 328: correct # of elements
for i, li in enumerate(li_elements[:6]):
    print(f"Title {i}: {li.find('h2')}")
# first 6 names look correct

# pull out the important elements
abstract_data = []
for li in li_elements:
    h2 = li.find('h2')
    
    # Find the <th> with sibling <th>Abstract</th>
    abstract_th = None
    abstract_sibling = li.find(lambda tag: tag.name == 'th' and tag.text == 'Abstract')
    if abstract_sibling and abstract_sibling.parent:
        abstract_th = abstract_sibling.parent.find('th')
    
    # Find the <th> with sibling <th>DOI</th>
    doi_th = None
    doi_sibling = li.find(lambda tag: tag.name == 'th' and tag.text == 'DOI')
    if doi_sibling and doi_sibling.parent:
        doi_th = doi_sibling.parent.find('th')

    # Append the data as a dictionary
    abstract_data.append({
        'h2': h2,
        'abstract_th': abstract_th,
        'doi_th': doi_th
    })
print(abstract_data[0])