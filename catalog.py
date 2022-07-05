#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi
sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.ProductCatalog import ProductCatalog


data = cgi.FieldStorage()

price_sort = data.getvalue('price_sort')

products = ProductCatalog.index(price_sort if price_sort != None else "asc")
print("Content-type: text/html; charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 
print() # \n -> Marks HTTP header end
#body

#print(price_sort)
print("<h2><div>SORT BY PRICE:  <a href='/web/catalog.py?price_sort=asc'> ▲ </a>  <a href='/web/catalog.py?price_sort=desc '>▼</a></div>")

# Product List
for product in products: 
    print(f"<h2>{ product.name :30}</h2>")
    print(f"<p><strong>{product.price_value:10}</strong>{product.price_unit}</p>")
    print(f"<p><a href='/web/details.py?id={product.id}'>Details</a></p>")
    print("<hr>")
    
#  browser -> text/plain

