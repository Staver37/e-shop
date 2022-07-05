#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi




# takes the input and puts it into the DATA variable
data = cgi.FieldStorage() # {id: }

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.CartManager import CartManager
product_id = data.getvalue('id')
CartManager.addItem(product_id)
# HW1: finish the addItem() method
print(f"Refresh: 3; URL=/web/details.py?id={product_id}")
print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

print() # \n -> Marks HTTP header end

print(f"Product {product_id}  HAS BEEN ADDED TO THE CART")
print(f"You will be redirected to the product page in 3 secounds")