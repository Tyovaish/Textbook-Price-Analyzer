import Scrapers
from Scrapers.AmazonScraper import findAmazonProductPrices
from Scrapers.EbayScraper import findEbayProductPrices


def findMinimumProductPrice(productsToSearch,productID,seller):
    minimumPriceProduct=[]
    for product in productsToSearch:
        if(product['productName']==productID and product['seller']==seller):
            minimumPriceProduct=product

    if not minimumPriceProduct:
        return

    for product in productsToSearch:
        if (product['productName'] == productID and product['seller']==seller and minimumPriceProduct['price']+minimumPriceProduct['shippingCost']>product['price']+product['shippingCost']):
            minimumPriceProduct = product

    return minimumPriceProduct

def removeProduct(productsToSearch,productToRemove):
    productsToSearch.remove(productToRemove);
    
def findPairToMaximizeProfitMargin(productsToSearch,productID):
    buyingFromMinimumProduct=findMinimumProductPrice(productsToSearch,productID,'Amazon')
    sellingToMinimumProduct=findMinimumProductPrice(productsToSearch,productID,'eBay')
    return buyingFromMinimumProduct,sellingToMinimumProduct

def mergeDatabase(productsToSearch1,productsToSearch2):
    for products in productsToSearch2:
        productsToSearch1.append(products)
    return productsToSearch1
