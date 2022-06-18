-- these scripts correspond to the APP LOGIC





-- HIGH LEVEL (APP) LOGIC
--  -----> translate
--                   ---> LOW LEVEL (DB LOGIC




/*
    ADMIN LOGIC
*/

-- Add product
INSERT  INTO "Product"
VALUES (1,'first name',100,'USD','1234567890123',10);
INSERT  INTO "Product"
VALUES (2,'secound name',200,'USD','2234567890123',20);
INSERT  INTO "Product"
VALUES (3,'thirth name',300,'USD','3234567890123',30);
INSERT  INTO "Product"
VALUES (4,'fourth name',400,'USD','4234567890123',40);
INSERT  INTO "Product"
VALUES (5,'fourth name',500,'USD','5234567890123',50);


/*
    CLIENT LOGIC
*/
--sign up
INSERT  INTO "Client"
VALUES (1,'First Client','First_Client@g.com','+123456789',true,'aaaa');

-- add to bag/ Tranzaction
--Start transaction

BEGIN ; 
INSERT  INTO "Bag"
VALUES (1,1);
--Commit/ roll back  transaction
INSERT  INTO "BagItem"
VALUES (1, 3, 10);

UPDATE "Product"
SET quantity = quantity - 10  
WHERE  id = 3;
COMMIT;


-- viw bag / not complete
SELECT * FROM "BagItem"
WHERE bag_id = 1;


/*
    API LOGIC
*/
