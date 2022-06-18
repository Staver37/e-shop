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
    #def  addProduct(product):
    #   if product == None:
    #        return Product.create()
    #    else:
    #       return True  
    #    
        
        
        # 1. check if the product exist in the table (doesnt work isProductAvailable)
        # 2. if it doest exist -> product.create()
        # 3. if it exist? - sum some quantity
        