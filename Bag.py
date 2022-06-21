import psycopg2
conn = psycopg2.connect("dbname=e_shop user=postgres ")
# Model 1
class Bag:

    def __init__(

        self,
            id,
            client_id
    ):

            self.id = id                    
            self.client_id = client_id

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
        sql = f"SELECT * FROM \"Bag\";"
        bags_list = Bag.executeFetchlSQL(sql)
        bags = []
        for bag_tuple in bags_list:
            #HW 1: try to optimize multiple parameters intro function
            bag = Bag(*bag_tuple)
            bags.append(bag)
        return  bags    
   
    def get(id):    
        sql = f"SELECT * FROM \"Bag\" WHERE id = {id};"       
        bag_l = Bag.executeFetchlSQL(sql)
        if len(bag_l) > 0:       
            bag_tuple = bag_l[0]
            bag = Bag(*bag_tuple)
            return  bag      
        else:
            return None

    def create(self):
       sql=(f"INSERT  INTO \"Bag\"VALUES ({self.id},{self.client_id});")
       conn.commit() 
       self.executeUpdateSQL(sql)

    def save(self):
       sql = f"UPDATE \"Bag\" SET client_id = {self.client_id} WHERE id = {self.id} ;"
       self.executeUpdateSQL(sql)
    
    def delete(self):
       sql = (f"DELETE  FROM \"Bag\" WHERE  id = {self.id};")
       self.executeUpdateSQL(sql)
    
    def __str__(self):
       return f"Bag id{self.id}"

    def __repr__(self):
         return str(self)               