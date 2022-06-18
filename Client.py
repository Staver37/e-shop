import psycopg2
conn = psycopg2.connect("dbname=e_shop user=postgres ")
# Model 1
class Client:

    def __init__(

        self,
            id,
            name,
            email,
            phone,
            is_vip,
            password
    ):

            self.id =id                    
            self.name = name
            self.email = email
            self.phone = phone
            self.is_vip = is_vip
            self.password = password
   
    def executeUpdateSQL(self,sql ):
       conn = psycopg2.connect("dbname=e_shop user=postgres ")
       cursor = conn.cursor()
       cursor.execute(sql)
       conn.commit() 
       cursor.close()
       conn.close()

    def executeFetchlSQL(sql):
       conn = psycopg2.connect("dbname=e_shop user=postgres ")
       cursor = conn.cursor()
       cursor.execute(sql)
       result = cursor.fetchall()
       return result
   
   
    def delete(self):
       sql = (f"DELETE  FROM \"Client\" WHERE  id = {self.id};")
       self.executeUpdateSQL(sql)
       
#
    def all():    
        sql = f"SELECT * FROM \"Client\";"
        clients_list = Client.executeFetchlSQL(sql)
        clients = []
        for client_tuple in clients_list:
            #HW 1: try to optimize multiple parameters intro function
            client = Client(
                 client_tuple[0],
                 client_tuple[1],
                 client_tuple[2],
                 client_tuple[3],
                 client_tuple[4],
                 client_tuple[5]
            )
            clients.append(client)
        return  clients    
 #
    
    def get(id):    
        sql = f"SELECT * FROM \"Client\" WHERE id = {id};"       
        client_l = Client.executeFetchlSQL(sql)
        if len(client_l) > 0:       
            client_tuple = client_l[0] # to optain ressult
            client = Client(
                  client_tuple[0],
                  client_tuple[1],
                  client_tuple[2],
                  client_tuple[3],
                  client_tuple[4],
                  client_tuple[5]
               )
            return  client      
        else:
            return None
#

    def create(self):
       sql=(f"INSERT  INTO \"Client\"VALUES ({self.id},'{self.name}','{self.email}','{self.phone}','{self.is_vip}','{self.password}');")
       conn.commit() 
       self.executeUpdateSQL(sql)


    def save(self):
       sql = f"UPDATE \"Client\" SET name = '{self.name}', email = '{self.email}',phone = '{self.phone}', is_vip = '{self.is_vip}', password = '{self.password}' WHERE id = {self.id} ;"
       self.executeUpdateSQL(sql)

    def __str__(self):
       return f"Client id{self.id}"

    def __repr__(self):
         return str(self)  


    # HW2:  complete the code for the models : Bag, BagItem, Client     