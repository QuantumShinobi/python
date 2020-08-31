#%%
import bs4
import requests
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup  = bs4.BeautifulSoup(res.text, "lxml")


# %%
soup.select(".thumbimage")
# %%
comp = soup.select(".thumbimage")[0]
comp['src']
# %%
img_link = requests.get("https:"+comp['src'])
# %%
# img_link.content
f = open("my_comp_img.jpg", "wb")
f.write(img_link.content)
# %%
f.close()
# %%
