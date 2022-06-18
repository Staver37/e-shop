CREATE TABLE "BagItem"
(
    bag_id        INTEGER  NOT NULL,
    product_id    INTEGER  NOT NULL, 
    quantity      INTEGER  DEFAULT 1
);


ALTER TABLE "BagItem"
ADD      CONSTRAINT fk_BagItem_Bag_id  FOREIGN  KEY (bag_id)
REFERENCES  "Bag"(id);

ALTER TABLE "BagItem"
ADD      CONSTRAINT fk_BagItem_produuct_id  FOREIGN  KEY (product_id)
REFERENCES  "Product"(id);










1.ACID - principles
Normalization  Forms (1NF..6NF)




HW1 : study the 1NF , 2NF