from lib.item import Item

class ItemRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM items')
        all_items = []
        for row in rows:
            item = Item(row["id"], row["item_name"], row["unit_price"], row["quantity"])
            all_items.append(item)
        return all_items

    def create(self, item):
        self._connection.execute('INSERT INTO items (item_name, unit_price, quantity) VALUES (%s,%s,%s)', ["Webcam", 25.50, 5])
        return None
