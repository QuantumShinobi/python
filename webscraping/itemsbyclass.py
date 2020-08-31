
# soup.select('div')
# soup.select("#id")
# soup.select(".class")
# soup.select("div span")
# 👆 this gives :-  all the spans in a div
# soup.select("div>span")
# 👆 this gives :-  all the spans direclty in a div

# %%
import bs4
import requests

# %%
res = requests.get("https://en.wikipedia.org/wiki/Visual_Studio_Code")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# %%
result = soup.select('.toctext')
# %%
for item in result:
    print(item.text)

# %%
