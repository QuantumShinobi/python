"""
AN INTRO TO :
WEB SCRAPING WITH PYTHON 
"""
# %%
# grabbing a page title (tooo simple)
import requests
import bs4
result = requests.get("https://www.example.com/")
type(result)
result.text

# %%
# creating a soup (which will convert the string into html )
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# lxml is the parsing engine which is to be used
soup = bs4.BeautifulSoup(result.text, "lxml")
soup

# %%
# to get items
title = soup.select("title")
# this 👆 returns a list
title[0].getText()
# %%
