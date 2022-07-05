## Shell path for MacOS
    psql: command not found Mac
     **  export PATH=/Library/PostgreSQL/9.5/bin:$PATH
     **  restart the terminal

     
## SQL Comands TERMINAL
  https://postgrescheatsheet.com/#/tables 
  https://www.postgresql.org/
  
     Postgres Path:           psql -U postgres 
     DB list :                \l
     Connected to DataBase:   \c
     ----------------------------
     CREATE DATABASE:         \h
     ---------------------------- 
     TABLE_NAME:              \d
     CREATE TABLE  "table_name"(colom1 TYPE PRIMARY KEY, colom2 TYPE CONSTRAIN);
     Open a table:  SELECT * FROM   "table_name"; 
     
     ALTER TABLE "Bag"
     ADD      CONSTRAINT fk_bag  FOREIGN  KEY (client_id)
     REFERENCES  "Client"(id);
        
        
        
        
        
        
      # NORMAL FORMS FOR  DB
    - First Normal Form (1NF)
      * All rows must be unique (no dublicate rows) /Eliminate duplicative columns from the same table.
      * Each cell must only contain a single value (not a list)
      * Each value should be atomic or non divisible (can't be split down futher) 
     
    - Second Normal Form (2NF)
        Second normal form (2NF) further addresses the concept of removing duplicative data:
      * Meet all the requirements of the first normal form.
      * Remove subsets of data that apply to multiple rows of a table and place them in separate tables.
      * Create relationships between these new tables and their predecessors through the use of foreign keys.
   
   
    - Third Normal Form (3NF)
       Third normal form (3NF) goes one significant step further:
       * Meet all the requirements of the second normal form.
       * Remove columns that are not dependent upon the primary key.
       
       
       
       # Boyce-Codd Normal Form (BCNF or 3.5NF)
           The Boyce-Codd Normal Form, also referred to as the "third and half (3.5) normal form," adds one more requirement:

       * Meet all the requirements of the third normal form.
       * Every determinant must be a candidate key.
    
    - Fourth Normal Form (4NF)
     Finally, fourth normal form (4NF) has one additional requirement:
      * Meet all the requirements of the third normal form.
      * A relation is in 4NF if it has no multi-valued dependencies.
      * Remember, these normalization guidelines are cumulative. For a database to be in 2NF, it must first fulfill all the criteria of a 1NF database.

        
        
        
        # A.C.I.D. properties: Atomicity, Consistency, Isolation, and Durability
        *Atomicity - each statement in a transaction (to read, write, update or delete data) is treated as a single unit. Either the entire statement is executed, or none of it is executed. This property prevents data loss and corruption from occurring if, for example, if your streaming data source fails mid-stream.
        
        *Consistency - ensures that transactions only make changes to tables in predefined, predictable ways. Transactional consistency ensures that corruption or errors in your data do not create unintended consequences for the integrity of your table.
        
        *Isolation - when multiple users are reading and writing from the same table all at once, isolation of their transactions ensures that the concurrent transactions don’t interfere with or affect one another. Each request can occur as though they were occurring one by one, even though they're actually occurring simultaneously.
        
        *Durability - ensures that changes to your data made by successfully executed transactions will be saved, even in the event of system failure.
