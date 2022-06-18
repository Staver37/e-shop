-- DDL instruction (CREATE, AFTER, DROP)
CREATE TABLE "Product"
(
id           integer               PRIMARY KEY,
name         character varying(121),
price_value  numeric,
price_unit   character varying(5),
bar_code     character varying(15)   UNIQUE ,
quantity     integer
);

DROP TABLE "Product";

ALTER TABLE "Product" ADD COLUMN bar_code character varying;
-- HW1:write an SQL script that will remove the bar_code column
ALTER TABLE "Product" DROP COLUMN bar_code;


INSERT INTO "Product" (id,name,price)VALUES (1,'First Product',100);
INSERT INTO "Product" (id,name,price)
VALUES (1,'First Product',100);
INSERT INTO "Product" (id,name,price)
VALUES (2,'Secound Product',200);
INSERT INTO "Product" (id,name,price)
VALUES (3,'Third Product',300);

-----------------------------------------
SELECT * FROM "Product";

SELECT * FROM "Product"
ORDER BY id ASC ;
--HW 2: write another select that mwill show only the product cheper that 250
SELECT * FROM "Product" 
WHERE price < 250;
------------------------------------------


UPDATE "Product"
set price = 0;

UPDATE "Product" 
set price = 300 
WHERE id = 3;

SELECT * FROM "Product"
ORDER BY id ASC ;

DELETE  FROM "Product"
WHERE id = 2;

