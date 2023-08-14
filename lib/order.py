
'''
Test file for Order object. 
Variables: 
id - serial
customer_name - text 
order_date - text
'''

class Order():
    def __init__(self, id, customer_name, order_date, item_id = None):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
        self.item_id = item_id or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"#{self.id} {self.customer_name} - Ordered On: {self.order_date}"