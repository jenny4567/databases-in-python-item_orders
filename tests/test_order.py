from lib.order import Order

'''
Test file for Order object. 
Variables: 
id - serial
customer_name - text 
order_date - text
'''

'''
Test initialisation of Order object with variables.
'''
def test_Order_init(db_connection):
    test_order = Order(1, "Ben MacIntyre", "12/04/23")
    assert test_order.id == 1
    assert test_order.customer_name == "Ben MacIntyre"
    assert test_order.order_date == "12/04/23"

'''
Test identical Orders are equivalent.
'''
def test_Order_equiv():
    test_order1 = Order(1, "Ben MacIntyre", "12/04/23")
    test_order2 = Order(1, "Ben MacIntyre", "12/04/23")
    assert test_order1 == test_order2

'''
Test Order prints in a suitable format.
'''
def test_Order_formatting():
    test_order = Order(1, "Ben MacIntyre", "12/04/23")
    assert str(test_order) == "#1 Ben MacIntyre - Ordered On: 12/04/23"