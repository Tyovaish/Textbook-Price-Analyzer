import urllib.request
from bs4 import BeautifulSoup
import re

def findAmazonProductPrices(productName):
    url="https://www.amazon.com/gp/offer-listing/"+productName+"/ref=olp_f_new?ie=UTF8&f_new=true&f_used=true&f_usedAcceptable=true&f_usedGood=true&f_usedLikeNew=true&f_usedVeryGood=true"
    while True:
        try:
            htmlfile = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        break

    soup = BeautifulSoup(htmlfile, 'html.parser')
    everything=soup.find_all('div',{"class":"a-row a-spacing-mini olpOffer"})
    productsImproved=[]
    for everythingData_tag in everything:
        priceData = everythingData_tag.find_all('span', {"class": "a-size-large a-color-price olpOfferPrice a-text-bold"})
        shipping = everythingData_tag.find_all('span', {"class": "olpShippingPrice"})
        condition = everythingData_tag.find_all('span', {"class": "a-size-medium olpCondition a-text-bold"})
        comments = everythingData_tag.find_all('div', {"class": "comments", "style": ""})
        shippingOnProduct=0
        priceDataOnProduct=0
        conditionOnProduct=''
        commentsOnProduct=''
        if priceData:
            priceDataOnProduct=float(priceData[0].text.strip()[1:])
        if shipping:
            shippingOnProduct=float(shipping[0].text.strip()[1:])
        if condition:
            conditionOnProduct = re.sub('[\s+]', '', condition[0].text.strip()).split('-')
        if comments:
            commentsOnProduct =comments[0].text.strip()
        productsImproved.append({'productName':productName,'productID':'0','price':priceDataOnProduct,'shippingCost':shippingOnProduct,'condition':conditionOnProduct,'comments':commentsOnProduct, 'seller':'Amazon', 'url':url})
    return productsImproved
