
'''
Item object file

Variables: 
id - serial
item_name - text 
unit_price - float
quantity - integer
'''

class Item():
    def __init__(self, id, item_name, unit_price, quantity):
        self.id = id
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"#{self.id} {self.item_name} - Unit Price: {self.unit_price} - Quantity: {self.quantity}"