DROP TABLE IF EXISTS items cascade;
DROP SEQUENCE IF EXISTS items_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;

CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name text,
    unit_price float,
    quantity integer
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date text,
    item_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade
);

INSERT INTO items (item_name, unit_price, quantity) VALUES ('TV', 319.99, 4);
INSERT INTO items (item_name, unit_price, quantity) VALUES ('Microwave', 99.99, 10);
INSERT INTO items (item_name, unit_price, quantity) VALUES ('Dishwasher', 450.00, 2);
INSERT INTO items (item_name, unit_price, quantity) VALUES ('Radio', 45.00, 13)