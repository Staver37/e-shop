#Model Uper Level (like for real life)

#from typing_extensions import Self
from .Product import Product


class ProductStock:
    
    def isProductAvailable(productId):
        product = Product.get(productId)
        if product == None:
            return False
        elif product.quantity == 0:
            return False
        else:
            return True     

# HW3: finish this metod

        # 1. check if the product exist in the table (doesnt work isProductAvailable)
        # 2. if it doest exist -> product.create()
        # 3. if it exist? -> sum some quantity
        
    def addProduct(addproduct):
        product = Product.get(addproduct.id)                                                                                     
        if product == None:    
            Product.create(addproduct)             
            

        else:
            ###########
            sql = f"UPDATE \"Product\" SET quantity \
                 = quantity + {addproduct.quantity} WHERE id = {product.id};"
            
            Product.executeUpdateSQL(sql)  
            ###########

# HW4: finish the method that removes the product complectly
    def removeProduct(productID):
        Product.delete(productID)

# HW5: finish the method that substract  a product quantity from stock prodbuct
    # - verifica daca este drodus in stock
    # - Update the quantity  
    # - Save
    
    def  subProductQuantity(id, amount):
        product = ProductStock.isProductAvailable(product.id)
        if product == True:
            sql = f"UPDATE product SET quantity = quantity - {amount} WHERE id = {product.id};"
            Product.executeUpdateSQL(sql)
        else:
            print("The product is not in stock!")