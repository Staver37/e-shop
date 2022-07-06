# HW2
#     - try to finish this class
from .BagItem import BagItem

# partial completed
class CartManager:
   
    def addItem(id):
        add_I = BagItem.create(id)
        return add_I

     #pass
    def removeItem(itemID):
        rem_I = BagItem.delete(itemID)
        return rem_I

    def updateItem(id):
        update_I = BagItem.save(id)
        return update_I


    def Clear():
        pass
        
    def viwCart():
        V_cart = BagItem.all()
        return V_cart


