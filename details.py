#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
import sys
import cgi


# takes the input and puts it into the DATA variable
data = cgi.FieldStorage() # {id:2}

sys.path.append("/Users/adrian/Desktop/PY-PROJECTS/Level 2/Data Base (DB)/e-shop")

from orm.ProductCatalog import ProductCatalog

product = ProductCatalog.details(data.getvalue('id'))
print("Content-type: text/html;charset=UTF-8") # -> HTTP Heder (encoding for PY to HTML) 

print() # \n -> Marks HTTP header end

print(f"<h1>{product.name}</h1>")
print(f"<h2>{product.price_value}{product.price_unit}</h2>")
print("<hr>")
print(f"<a href='/web/add-to-cart.py?id={product.id}'>Add to: 🛒</a>")