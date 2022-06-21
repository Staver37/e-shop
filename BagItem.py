import psycopg2
conn = psycopg2.connect("dbname=e_shop user=postgres ")
# Model 1
class BagItem:

    def __init__(

        self,
            bag_id,
            product_id,
            quantity
    ):

            self.bag_id = bag_id                    
            self.product_id = product_id
            self.quantity = quantity

    def executeUpdateSQL(self,sql ):
       conn = psycopg2.connect("dbname=e_shop user=postgres ")
       cursor = conn.cursor()
       cursor.execute(sql)
       conn.commit() 
       cursor.close()
       conn.close()
    
    def executeFetchlSQL(sql ):
       conn = psycopg2.connect("dbname=e_shop user=postgres ")
       cursor = conn.cursor()
       cursor.execute(sql)
       result = cursor.fetchall()
       return result
     
    def all():    
        sql = f"SELECT * FROM \"BagItem\";"
        bagsI_list = BagItem.executeFetchlSQL(sql)
        bagsI = []
        for bagI_tuple in bagsI_list:
            #HW 1: try to optimize multiple parameters intro function
            bagI = BagItem(*bagI_tuple)
            bagsI.append(bagI)
        return  bagsI    

    def get(bag_id):    
        sql = f"SELECT * FROM \"BagItem\" WHERE bag_id = {bag_id};"       
        bagI_l = BagItem.executeFetchlSQL(sql)
        if len(bagI_l) > 0:       
            bagI_tuple = bagI_l[0] 
            bagI = BagItem(*bagI_tuple)
            return  bagI      
        else:
            return None     

    def create(self):
       sql=(f"INSERT  INTO \"BagItem\"VALUES ({self.bag_id},{self.product_id},{self.quantity});")
       conn.commit() 
       self.executeUpdateSQL(sql)

    def save(self):
       sql = f"UPDATE \"BagItem\" SET product_id = {self.product_id} , quantity = {self.quantity} WHERE bag_id = {self.bag_id} ;"
       self.executeUpdateSQL(sql)
    
    def delete(self):
       sql = (f"DELETE  FROM \"BagItem\" WHERE  bag_id = {self.bag_id};")
       self.executeUpdateSQL(sql)





    def __str__(self):
       return f"bag_id :  {self.bag_id}"

    def __repr__(self):
         return str(self)                    