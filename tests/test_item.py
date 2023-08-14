from lib.item import Item

'''
Test file for Item object. 
Variables: 
id - serial
item_name - text 
unit_price - float
quantity - integer
'''

'''
Test initialisation of Item object with variables.
'''
def test_Item_init(db_connection):
    test_item = Item(1, "TV", 319.99, 4)
    assert test_item.id == 1
    assert test_item.item_name == "TV"
    assert test_item.unit_price == 319.99
    assert test_item.quantity == 4

'''
Test identical Items are equivalent.
'''
def test_Item_equiv():
    test_item1 = Item(1, "TV", 319.99, 4)
    test_item2 = Item(1, "TV", 319.99, 4)
    assert test_item1 == test_item2

'''
Test Item prints in a suitable format.
'''
def test_Item_formatting():
    test_item = Item(1, "TV", 319.99, 4)
    assert str(test_item) == "#1 TV - Unit Price: 319.99 - Quantity: 4"