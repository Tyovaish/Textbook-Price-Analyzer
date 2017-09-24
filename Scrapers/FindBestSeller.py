import urllib.request
from bs4 import BeautifulSoup
import json

from Scrapers.AmazonScraper import findAmazonProductPrices


def findBestAmazonBestSellerProducts(url,productList):
    while True:
        try:
            htmlfile = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        break

    soup = BeautifulSoup(htmlfile, 'html.parser')
    everything = soup.find_all('div', {"class": "a-section a-spacing-none p13n-asin"})
    for everything_Data in everything:
        productList.append(json.loads(everything_Data.get('data-p13n-asin-metadata'))['asin'])

def findBestAmazonSellersAmazon():
    url='https://www.amazon.com/Best-Sellers-Books-Textbooks/zgbs/books/465600/ref=zg_bs_nav_b_1_b'
    while True:
        try:
            htmlfile = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        break

    soup = BeautifulSoup(htmlfile, 'html.parser')
    everything = soup.find_all('ul', {"id": "zg_browseRoot"})
    linksToUrls=[]
    linksToSearch=[]
    productIDs=[]
    for everything_Data in everything:
        linksToUrls=everything_Data.find_all('a')
    for everything_Data in linksToUrls:
        linksToSearch.append(everything_Data.get('href'))
    linksToSearch=linksToSearch[2:]
    print (linksToSearch)
    for links in linksToSearch:
        findBestAmazonBestSellerProducts(links,productIDs)
    return productIDs