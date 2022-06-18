from os import system
system("clear")
from orm. Product import Product
from orm.ProductStock import ProductStock
from orm.Client import Client
from orm.Bag import Bag
from orm.BagItem import BagItem
#                 ProductStock
#   Model  - for orm (High level) call           
##############################################################
#     Is Product Available -> True / False
available = ProductStock.isProductAvailable(4)
print(available)

##############################################################



#           Model  - for orm (low level) call
#                       Product    
#   Model  - for orm (low level) call           
##################################################################
  # Create
#c = Product(6, "sixht name", 600, "USD", "6234567890123", 60)
#c.create()

  #Alterate and save
#a_p = Product(1, "First name", 100, "USD", "1234567890123", 0)
#a_p.quantity = 0
#a_p.save()

 # Dellete 
#d_p = Product(6, "xxx", 000, "xxx", "0000000000000", 00)
#d_p.delete()

 # Print by Index
#g_p = Product.get(6)
#print(f"{g_p.name},{g_p.quantity}")
#print(type(g_p))
   
   # Print All Products
#all_p = Product.all()
#print(type(all_p))
#print(all_p)
################################################################

#                Client
##########################################
#      Create Client
#c_c = Client(3, "Third name", "Third_Client@g.com" , +223456789, "f", "bbbbbb")
#c_c.create()

#      Print All Clients
#a_c = Client.all()
#print(type(a_c))
#print(f"{a_c}")

#      Print Client by Index
#g_c = Client.get(3)
#print(f"Name:{g_c.name},  Email:{g_c.email}")

 #     Dellete  Client
#d_c = Client(3, "xxx", 000, "xxx", "0000000000000", 00)
#d_c.delete()
  
#      Alterate and save Client
#a_c = Client(2, "Secound name", "Third_Client@g.com " , "+323456789", "f", "aab5138aba")
#a_c.password = "bababa"
#a_c.save()

##########################################

#                Bag
##########################################
#       Create Bag
#c_b = Bag(4,3)
#c_b.create()

#      Print All Bags
#a_b = Bag.all()
#print(type(a_b))
#print(f"{a_b}")

#       Print Bag by Index
#g_b = Bag.get(3)
#print(f"Bag ID:{g_b.id}, Client ID: {g_b.client_id}")

#       Dellete  Bag by Index 
#d_b = Bag(3,0)
#d_b.delete()

#       Alterate and save Bag
#a_b = Bag(1,0)
#a_b.client_id = 1
#a_b.save()
##########################################

#                BagItem
##########################################
#      Print All Bags
#a_b = BagItem.all()
#print(type(a_b))
#print(f"{a_b}")

#       Print Bag Item by Index
#g_bI = BagItem.get(1)
#print(f"Bag ID:{g_bI.bag_id},   Product ID:{g_bI.product_id},  Quantity:{g_bI.quantity} ")

#                    Create BagItem
#            bag_id | product_id | quantity 
#               v        v            v
#c_bI = BagItem(4,       4 ,         20)
#c_bI.create()

#       Alterate and save BagItem
#a_bI = BagItem(2,"x","x")
#a_bI.product_id = 3
#a_bI.quantity = 7
#a_bI.save()

#       Dellete  BagItem by Index 
#             bag_id 
#               v
#d_bI = BagItem(4,0,0)
#d_bI.delete()
##########################################
























#from os import system
#import psycopg2

#conn = psycopg2.connect("dbname=e_shop user=postgres ")
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM  "Product";')
#cursor.execute("INSERT  INTO Product(id,name,price_value,price_unit,bar_code,quantity) VALUE (%s,%s)" (5,"fiveth name",500,"USD" , '5234567890123',50))
#conn.commit()

# returns a list of tupless

# HW2 study the tuples / diffs against list
# HW3 try to execute from python all the DOMAIN instruction, try input values from kb

#products = cursor.fetchall()
#system ("clear")
#for product in products:
#    print(product)
     
    

    
   

    




