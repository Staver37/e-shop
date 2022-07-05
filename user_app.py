from os import  system
system("clear")
from orm. Product import Product
from orm.ProductStock import ProductStock
from orm.Client import Client
from orm.Bag import Bag
from orm.BagItem import BagItem


#                 ProductStock
#   Model  - for Domain (High level) call           
##############################################################
#                 Is Product Available -> True / False
#available = ProductStock.isProductAvailable(2)
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
#c_p = Product(6, "sixht name", 600, "USD", "6234567890123", 60)
#c_p.create()

        #Alterate and save
#a_p = Product(3, "Third name", 300, "USD", "3234567890123", 30)
#a_p.name = "Third name"
#a_p.save()

        # Dellete 
#d_p = Product(11, "xxx", 000, "xxx", "0000000000000", 00)
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
#c_c = Client(3, "thirdth Client", "t_Client@g.com" , "+1223456789", "t", "dacytxc")
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
#d_b = Bag(4,0)
#d_b.delete()

#       Alterate and save Bag
#a_b = Bag(1,0)
#a_b.client_id = 1
#a_b.save()
################################################################

#                BagItem
################################################################
#      Print All Bags
#a_b = BagItem.all()
#print(type(a_b))
#print(f"{a_b}")

#       Print Bag Item by Index
#g_bI = BagItem.get(1)
#print(f"Bag ID:{g_bI.bag_id}, Product ID:{g_bI.product_id},  Quantity:{g_bI.quantity} ")

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
#d_bI = BagItem(5,0,0)
#d_bI.delete()
################################################################











# typical exemple
# APP -> memory ->task
# CRUD / BREAD
from os import system
# MAIN LOOP  ######################################
while True:
    system("clear")
    print("MENU")
    print("1. Produs")    
    print("2. Client")
    print("3. Bag")
    print("4. Bag Item")
    print("0. Exit")
    option = int(input(">>"))
    if option == 1:
        system("clear")



    while True:
        system("clear")
        print("MENU")
        print("1. add Produs")    
        print("2. Show Produs")
        print("3. Remove Produs")
        print("4. Change Produs")
        print("5. Swap task A with Task B")
        print("0. Exit")
        option = int(input(">>"))
        if option == 1:
            system("clear")
    # Add TASKS ######################################
            
            while True:
                id = input("ID:   ")
                name = input("Name:   ")
                value = input("Value:   ")
                cur = input("Curency:   ")
                bar_code = input("Bar Code:   ")
                quantity = input("Quantity:   ")

            #c_p = Product(6, "sixht name", 600, "USD", "6234567890123", 60)
            #c_p.create() 
                c_p = Product(id, name, value,  cur,  bar_code, quantity)
                c_p.create()

            


                if new_task == " ":
                    break
                #if new_task not in tasks:
                #    tasks.append( new_task )
    # PRINT TASKS ######################################
        if option == 2:
            system("clear")
            print("\nYour tasks: ")

            for i in range(len(tasks)):
                print(i+1,">>>>>",tasks[i])
            input("\nHit ENTER to continue")

    # REMOVE A TASK ####################################       
    # HW1  p 3 ask for the index -> remove / python list metods
    #     * print the task title / confirm yes/no ? 
        
        if option == 3:
            system("clear")
            while True:
                id = input("ID:   ")
                ps_dell =Product(id,"x",0, "0","0",0) 
                ProductStock.removeProduct(ps_dell)

                #if i == " ":
                #    break
                 
    # EDIT A TASK ####################################       
        if option == 4:    
            system("clear")
            index = int(input("Enter task position:"))-1
            new_task = input("Enter edited task: ")
            tasks[index] = new_task

    # HW 2 +p 5 swap taskA with taskB -> indexA, indexB
        if option == 5:
            system("clear")
            i1 =int(input("Enter Task A: "))
            print(tasks[i1-1])
            i2 =int (input("Enter Task B: "))
            print(tasks[i2-1])
            tasks[i1-1],tasks[i2-1] = tasks[i2-1],tasks[i1-1]      
    # Exit ########################################## 
        if option == 0:            
            break
        
    
