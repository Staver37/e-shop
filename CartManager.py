# HW2
#     - try to finish this class
from .BagItem import BagItem

# partial completed
class CartManager:
    def addItem(id):
       BagItem.create(id)
     #pass
    def removeItem(itemID):
        BagItem.delete(itemID)

    def updateItem(id):
        BagItem.save(id) 


    def Clear():
        pass
        

    def viwCart(id):
        BagItem.all()


