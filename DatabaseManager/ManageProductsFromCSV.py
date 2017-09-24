
import pandas
import csv
def addProductsFromCSV(productsToSearch,productCSVFile):
    productsToSearchFromCSV=pandas.read_csv(productCSVFile)
    for index, row in productsToSearchFromCSV.iterrows():
        productsToSearch.append({'ProductName':row['ProductName'],'ProductID':row['ProductID']})


def addProductsFromUserInput(productsToSearch,productName,productID):
    productsToSearch.add({'ProductName':productName,'ProductID':productID})

def storeProductToCSV(productsToSearch):
    with open('mainProductsToSearch.csv', 'w') as csvfile:
        fieldnames = ['ProductName', 'ProductID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for productsToSearchItems in productsToSearch:
            writer.writerow({'ProductName':productsToSearchItems['productName'],'ProductID':productsToSearchItems['productID']})