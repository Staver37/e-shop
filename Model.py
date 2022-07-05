import psycopg2

class Model:
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