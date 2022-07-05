from http import client
from os import  system
from re import X
from orm.CartManager import CartManager
system("clear")
from orm. Product import Product
from orm.ProductStock import ProductStock
from orm.Client import Client
from orm.Bag import Bag
from orm.BagItem import BagItem



#                 CartManager
#   Model  - for Domain (High level) call           
##############################################################
#               Wiev all items in Cart





#                ADD Item in Cart
#add_I = BagItem(1, 2, 10)
#CartManager.addItem(add_I)


#                Remove Item by ID
#R_I =BagItem(4,"x","x") 
#CartManager.removeItem(R_I)


#                Update Item by ID

#u_i = BagItem(3,2,10)  
#CartManager.updateItem(u_i)

##############################################################






#                 ProductStock
#   Model  - for Domain (High level) call           
##############################################################
#                 Is Product Available -> True / False
#available = ProductStock.isProductAvailable(1)
#print(available)


#                add_p Produs
#add_p = Product(10, "four ", 100, "UDS", "1234567890123", 10)
#ProductStock.addProduct(add_p)


#                Remove Product by ID
#ps_dell =Product(6,"x",0, "0","0",0) 
#ProductStock.removeProduct(ps_dell)


#        substract  a Product from the Stock
#p1 = Product(5, "Product", 100, "UDS", "", 100)
#ProductStock.subProduct(p1, 5)



##############################################################
##############################################################
##############################################################




#           Model  - for orm (low level) call
#                       Product    
#   Model  - for orm (low level) call           
##############################################################
        # Create
#c_p = Product(9, "9th name", 900, "USD", "9234567890123", 80)
#c_p.create()

        #Alterate and save
#a_p = Product(3, "Third name", 400, "USD", "3234567890123", 30)
#a_p.name = "Third name"
#a_p.save()

        # Dellete 
#d_p = Product(6, "xxx", 000, "xxx", "0000000000000", 00)
#d_p.delete()

        # Print by Index
#g_p = Product.get(2)
#print(f"Product Name:  {g_p.name}, Quantity: {g_p.quantity}, Price Value: {g_p.price_value}")
#print(type(g_p))

        # Print All Products
#all_p = Product.all()
#print(type(all_p))
#print(all_p)
################################################################


#                Client
################################################################
          # Create Client
#c_c = Client(4, "Four Client", "f_Client@g.com" , "+4223456789", "t", "hasg41")
#c_c.create()

          # Print All Clients
#a_c = Client.all()
#print(type(a_c))
#print(f"{a_c}")

            # Print Client by Index
#g_c = Client.get(2)
#print(f"Name: {g_c.name} |  Email:{g_c.email} | Phone :'{g_c.phone}' |  Is_vip:{g_c.is_vip} |  Password:{g_c.password}")
#print(len(g_c.password))
 #     Dellete  Client
#d_c = Client(1, "xxx", 000, "xxx", "0000000000000", 00)
#d_c.delete()
  
#      Alterate and save Client
#a_c = Client(2, "Secound name", "Third_Client@g.com " , "+323456789", "f", "aab5138aba")
#a_c.password = "bababa"
#a_c.save()

################################################################

#                 Bag
################################################################
#       Create Bag
#c_b = Bag(4,1)
#c_b.create()

#      Print All Bags
#a_b = Bag.all()
#print(type(a_b))
#print(f"{a_b}")

#       Print Bag by Index
#g_b = Bag.get(3)
#print(f"Bag ID:{g_b.id}, Client ID: {g_b.client_id}")

#       Dellete  Bag by Index 
#d_b = Bag(4,0)
#d_b.delete()

#       Alterate and save Bag
#a_b = Bag(1,0)
#a_b.client_id = 1
#a_b.save()
################################################################

#                BagItem
################################################################

#       Print Bag Item by Index
#g_bI = BagItem.get(1)
#print(f"Bag ID:{g_bI.bag_id}, Product ID:{g_bI.product_id},  Quantity:{g_bI.quantity} ")

#                    Create BagItem
#            bag_id | product_id | quantity 
#               v        v            v
#c_bI = BagItem(2,        2 ,         2)
#c_bI.create()



#       Alterate and save BagItem
#a_bI = BagItem(2,"x","x")
#a_bI.product_id = 3
#a_bI.quantity = 7
#a_bI.save()

#       Dellete  BagItem by Index 
#             bag_id 
#               v
#d_bI = BagItem(1,2,50)
#d_bI.delete()

#      Print All Bags
#a_b = BagItem.all()
#print(type(a_b))
#print(f"{a_b}")
################################################################








































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
     
    

    
   

    




