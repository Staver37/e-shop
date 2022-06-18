







## Working with database  engine

                Conection
                    v                      ----------------------
[client app]<-------------->               |    PostgresSQL
                    *hierarhy (database>table>row>col)
                                           |    (server app)
                                           |   * data types
                                           ----------------------
                                              * DDL instructions
                                                     ^
                                                            * DML
                                                      instructions
                                                     |
                                                     v
                                                ------------
                                                |   data   |
                                                -------------
                                                



 ## Domain
    * Product
        + id        | int
        + name      | str
        + price     | float
        + bar_code  | str
-- HW1:write an SQL script that will remove the bar_code column
-- HW3: Create the clients table with the next structure     
    * Client
        * id
        * name
        * is_vip
        HW4 insert a few clients
        HW5:select only the clients wich name have leas 5 characters
        HW6:delete a client based on it's id
        HW7: show only the non-vip clients
        
    * Bag

    - Category
    - Paymant
    - ....
-- HW1:write an SQL script that will remove the bar_code column
-- HW3: Create the clients table with the next structure  
    HW4 insert a few clients
    HW5:select only the clients wich name have leas 5 characters
    HW6:delete a client based on it's id
    HW7: show only the non-vip clients
    HW8: alter the client's table add the email column

## Domain

* Product
    + id            | int                   |PK    (Primary Key)
    + name  name    | str
    + price_value   | float
    + price_unit    | str
    + bar_code      | str
    + quantity      | int     


* Client
    + id      integer     PK        <----------
    + name    character varying(61)            |
    + email   character varying(121)   UNIQUE, |
    + phone   character varying(21),           |
    + is_vip   boolean      DEFAULT False      |    
                                               | 
* Bag                                          |
    + id                                       | 
    + client_id ------------- relation/refrence   FK (Foreign key)
    
    
* BagItem
    + Bag_id             FK
    + product_id         FK
    + quantity
    


- Category
- Paymant
