# %%
import requests
import bs4
# url for home page = http://books.toscrape.com/
# url for 2nd page = http://books.toscrape.com/catalogue/page-2.html
# 👇 using .format method
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# %%
# page_num = 12
# print(base_url.format(page_num))
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
# %%
products = soup.select(".product_pod")
example = products[0]

# %%
example
# %%
# 1st way( wont work always)
# 'star-rating Two' in str(example)
# %%
# 2nd method (recommended)
[] == example.select(".star-rating.Three")
a = example.select("h3 a")
a[0]['title']
# %%
# DOING THE ABOVE METHOD FOR ALL THE BOOKS
two_star_title = []
for n in range(1, 51):
    scrap_url = base_url.format(n)
    res = requests.get(scrap_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.start-rating.Two')) != 0:
            title = book.select("h3 a")[0]['title']
            two_star_title.append(title)


# %%
print(two_star_title)

# %%
