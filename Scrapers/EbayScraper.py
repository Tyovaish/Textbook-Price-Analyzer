import re
import urllib.request
from bs4 import BeautifulSoup
import re
def findEbayProductPrices(productName):
    savedProductName=productName
    productName=productName.split()
    productKeywordSearch=""
    start=True
    for i in productName:
        if start:
            productKeywordSearch+=i
            start=False
        else:
            productKeywordSearch+=i+"+"
    url="https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw="+productKeywordSearch+"&_sop=15"
    while True:
        try:
            htmlfile = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        break
    soup = BeautifulSoup(htmlfile, 'html.parser')
    everything=soup.find_all('ul',{"class":"lvprices left space-zero"})
    productsImproved=[]
    for everythingData_tag in everything:
        priceData = everythingData_tag.find_all('li', {"class": "lvprice prc"})
        shipping = everythingData_tag.find_all('li', {"class": "lvshipping"})
        condition = everythingData_tag.find_all('span', {"class": "a-size-medium olpCondition a-text-bold"})
        comments = everythingData_tag.find_all('div', {"class": "comments", "style": ""})
        shippingOnProduct=0
        priceDataOnProduct=0
        conditionOnProduct=''
        commentsOnProduct=''
        if priceData:
            price = re.findall("\d+\.\d+", priceData[0].text.strip())
            if price:
                priceDataOnProduct = float(price[0])
            else:
                priceDataOnProduct = 0
        if shipping:
            shippingPrice=re.findall("\d+\.\d+",shipping[0].text.strip())
            if shippingPrice:
                shippingOnProduct=float(shippingPrice[0])
            else:
                shippingOnProduct=0
        if condition:
            conditionOnProduct = re.sub('[\s+]', '', condition[0].text.strip()).split('-')
        if comments:
            commentsOnProduct =comments[0].text.strip()
        productsImproved.append({'productName':savedProductName,'price':priceDataOnProduct,'shippingCost':shippingOnProduct,'condition':conditionOnProduct,'comments':commentsOnProduct, 'seller':'eBay', 'url':url})
    return productsImproved