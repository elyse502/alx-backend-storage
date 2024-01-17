-- A SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrement_order AFTER INSERT on orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
