
from .Product import Product
class ProductCatalog:
    
    def index(price_sort):
        products = Product.all(price_sort)
        return products

    def details(id):
        product = Product.get(id)
        return product