import bs4
import requests
from datetime import datetime
import csv


prod_urls = []
prod_names = []

url = "https://www.stihlusa.com/products/stihl-top-rated-products/"
ss = requests.get(url)
src = ss.text
soup = bs4.BeautifulSoup(src, "html.parser")

for a in soup.findAll('a', attrs={'class' : 'clickable-product-element'}):
    if a['href'] not in prod_urls:
        prod_urls.append(a['href'])
    if a.img:
        prod_names.append(a.img['title'])


# print ("prod_urls are: ", prod_urls)
# print ("prod_names are: ", prod_names)

prod_data = list(zip(prod_names, prod_urls))

print(prod_data)
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['productName','productUrl','time'])
    # The for loop
    for name, url in prod_data:
        writer.writerow([name, url, datetime.now()])

