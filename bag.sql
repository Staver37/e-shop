CREATE TABLE "Bag"
(
id          INTEGER  PRIMARY KEY ,
client_id   INTEGER  NOT NULL 

--CONSTRAINT fk_bag  FOREIGN  KEY (client_id)
--REFERENCES  Client(id)
);

ALTER TABLE "Bag"
ADD      CONSTRAINT fk_bag  FOREIGN  KEY (client_id)
REFERENCES  "Client"(id);