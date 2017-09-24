from tkinter import filedialog
from tkinter import *
from Scrapers.AmazonScraper import *
from Scrapers.FindBestSeller import *

safetyMargin = [.5]

def displayPopUpData(buyingProduct):
    top = Toplevel()
    top.title("Info")
    seller = Label(top,text="Seller:"+buyingProduct['seller'])
    price=Label(top,text="Price: $"+str(buyingProduct['price']))
    shippingCost = Label(top,text="Shipping Cost: $" + str(buyingProduct['shippingCost']))
    totalCost = Label(top,text="Total Cost: $" + str(round(buyingProduct['shippingCost'] + buyingProduct['price'],2)))
    condition=Label(top,text="Condition: "+str(buyingProduct['condition'][1]))
    comments=Label(top,text="Comments:\n"+buyingProduct['comments'])
    report=Button(top,text="Report",command=top.destroy)
    seller.pack()
    price.pack()
    shippingCost.pack()
    totalCost.pack()
    condition.pack()
    comments.pack()
    report.pack()

def displaySafetyMarginEntryBox(root,safetyMargin):
    top = Toplevel(root)
    Label(top, text="Safety Margin:").grid(row=0)
    safetyMarginEntry=Entry(top)
    safetyMarginEntry.grid(row=0, column=1)
    Button(top,text="Done",command=lambda: editSafetyMargin(top,safetyMargin,safetyMarginEntry.get())).grid(row=1,column=1)
    run(root);

def getbuyingProductsFromCSVFile(root):
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("csv files", "*.csv"),("all files","*.*")))


def displaybuyingProductUserEntryBox(root):
    top = Toplevel(root)
    Label(top, text="buyingProduct Name:").grid(row=0)
    Label(top,text="buyingProduct ID:").grid(row=1)
    buyingProductNameEntry=Entry(top)
    buyingProductIDEntry=Entry(top)
    buyingProductNameEntry.grid(row=0,column=1)
    buyingProductIDEntry.grid(row=1,column=1)
    Button(top,text="Done").grid(row=2,column=1)

def editSafetyMargin(top,safetyMargin,newSafetyMargin):
    safetyMargin[0]=float(newSafetyMargin)
    top.destroy()
    run(root)

def potentialPurchasingSitebProductData(root,buyingProduct,sellingProduct,startingRow,startingColumn):
    totalBuyingPrice=round(buyingProduct['price'] + buyingProduct['shippingCost'], 2)
    totalSellingPrice=round(sellingProduct['price'] + sellingProduct['shippingCost'], 2)
    profitMargin=round((totalSellingPrice-totalBuyingPrice)/totalBuyingPrice,5)
    Label(root, text="Product: " + buyingProduct['productName']).grid(row=startingRow, column=startingColumn)
    Label(root, text="Buy From: "+buyingProduct['seller']).grid(padx=10, row=startingRow, column=startingColumn+1)
    Label(root, text="Sell To: " + buyingProduct['seller']).grid(padx=10, row=startingRow, column=startingColumn + 2)
    Label(root,text="Total Buying Price: $" + str(totalBuyingPrice)).grid(padx=10, row=startingRow, column=startingColumn+3)
    Label(root, text="Total Selling Price: $" + str(totalSellingPrice)).grid(padx=10,row=startingRow,column=startingColumn + 4)
    Label(root,text="Profit Margin: "+str(profitMargin)).grid(padx=10,row=startingRow,column=startingColumn+5)
    Label(root, text="BUYING RISK", bg="red").grid(padx=10, row=startingRow, column=startingColumn+6)
    Label(root, text="SELLING RISK", bg="green").grid(padx=10, row=startingRow, column=startingColumn+7)
    Button(root, text="Get Buying Info", command=lambda: displayPopUpData(buyingProduct)).grid(padx=10,row=startingRow,column=startingColumn+8)
    Button(root, text="Get Selling Info", command=lambda: displayPopUpData(sellingProduct)).grid(padx=10,row=startingRow,column=startingColumn + 9)
    Button(root, text="Purchase").grid(padx=10,row=startingRow,column=startingColumn + 10)

def displayMenu(root,safetyMargin):
    menubar = Menu()
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Insert buyingProducts",command=lambda: displaybuyingProductUserEntryBox(root))
    filemenu.add_command(label="Insert buyingProducts From CSV", command=lambda: getbuyingProductsFromCSVFile(root))
    filemenu.add_command(label="Save buyingProducts")
    menubar.add_cascade(label="Insert", menu=filemenu)
    editMenu = Menu(menubar, tearoff=0)
    editMenu.add_command(label="Edit Safety Margin", command=lambda: displaySafetyMarginEntryBox(root,safetyMargin))
    menubar.add_cascade(label="Edit", menu=editMenu)
    root.config(menu=menubar)
#def gatherProductList(root,productList):

def run(root):
    buyingProducts=findAmazonProductPrices('B00KAED850')
    displayMenu(root,safetyMargin)
    potentialPurchasingSitebProductData(root,buyingProducts[1],buyingProducts[2],0,0)
root=Tk()
database=[{}]
run(root)
mainloop()