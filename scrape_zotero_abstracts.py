'''
 # @ File Name: scrape_zotero_abstracts
 # @ Author: Alexander Karl
 # @ Create Time: 2025-01-13
 # @ Description: Scrape Abstracts and 
 '''

# 0. Overhead
from bs4 import BeautifulSoup
import numpy as np
import pickle
import pandas as pd

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
article_data = []
for li in li_elements:
    # Extract content of the <h2> tag
    h2_content = li.find('h2').get_text(strip=True) if li.find('h2') else None
    
    # Find and extract the content of the Abstract's sibling
    abstract_sibling = li.find(lambda tag: tag.name == 'th' and tag.text == 'Abstract')
    abstract_content = (
        abstract_sibling.find_next_sibling('td').get_text(strip=True)
        if abstract_sibling and abstract_sibling.find_next_sibling('td')
        else None
    )
    
    # Find the DOI's sibling and extract the href URL
    doi_sibling = li.find(lambda tag: tag.name == 'th' and tag.text == 'DOI')
    doi_url = (
        doi_sibling.find_next_sibling('td').find('a')['href']
        if doi_sibling and doi_sibling.find_next_sibling('td') and doi_sibling.find_next_sibling('td').find('a')
        else None
    )
    
    # Append the extracted data as a dictionary
    article_data.append({
        'title': h2_content,
        'abstract_content': abstract_content,
        'doi_url': doi_url
    })

print(article_data[0])
#looks good

# check the DOIs. How many are missing
print(np.mean([1 if article['doi_url'] is not None else 0 for article in article_data]))
# 92% have DOI
print(sum([1 if article['doi_url'] is None else 0 for article in article_data]))
# 26 articles have no DOI, which is low enough to manually locate, but high enough to be tedious
# I don't specifically need DOIs, I likely don't need a unique identifier at all, it's just good practice to have one
# In case it's an issue, I'll stick a meaningless ID one on anyway
for i in range(len(article_data)):
    article_data[i]['NODOI'] = i

# save this as a python object
with open('raw_article_data.pkl', "xb") as outp:

    pickle.dump(article_data, outp)

# save as an excel file too, in case manual review is needed
article_df = pd.DataFrame(article_data)
article_df.to_excel("raw_article_data.xlsx", index=False)

# Next, move to a separate file for LDA