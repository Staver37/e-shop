Client.sql

CREATE  TABLE "Client" 
(
    id       integer                  PRIMARY KEY , 
    name     character varying(61),
    email    character varying(121)   UNIQUE, 
    phone    character varying(21),
    is_vip   boolean                  DEFAULT False
    
);



ALTER TABLE "Client" 
ADD COLUMN   password   CHAR(60);



DROP TABLE "Client";


INSERT INTO "Client"
(id,name, is_vip )values (1,'Adrian Staver',Adr@ , true);




INSERT INTO "Client"(id,name, is_vip )values (2,'Dorin Esinenco' , true);
INSERT INTO "Client"(id,name, is_vip,)values (3,'Vania Bat' , False);
INSERT INTO "Client"(id,name, is_vip )values (4,'Jora Carvan' , true);


SELECT * from "Client";
SELECT SUBSTRING("name", 1, 5) AS "Client";
FROM Customers;




DELETE FROM "Client" WHERE id = 4;

SELECT * FROM  "Client" WHERE  is_vip = false;

ALTER TABLE "Client" ADD Email  character varying;
UPDATE "Client" SET Email = 'AdrianStaver@gmal.com' WHERE id = 1;
UPDATE "Client" SET Email = 'DorinEsinenco@gmal.com' WHERE id = 2;
UPDATE "Client" SET Email = 'VaniaBat@gmal.com' WHERE id = 3;


INSERT INTO "Client"(id,name, is_vip,email)values (4,'Lena W' , False,'LenaW@gmal.com');

INSERT INTO "Client"(id,name, is_vip,email)values (5,'Joe S' , False,'JoeS@gmal.com');
UPDATE "Client" SET name = 'Joe S' WHERE id = 5;
UPDATE "Client" SET email = 'JoeS@goz.com' WHERE id = 5;

