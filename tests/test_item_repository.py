from lib.item import Item
from lib.item_repository import ItemRepository

'''
Test display all Item objects.
'''
def test_Item_all_function(db_connection):
    db_connection.seed("seeds/item_order_seed.sql")
    repository = ItemRepository(db_connection)
    assert repository.all() == [
        Item(1, "TV", 319.99, 4),
        Item(2, "Microwave", 99.99, 10),
        Item(3, "Dishwasher", 450.00, 2),
        Item(4, "Radio", 45.00, 13)
    ]

'''
Test creating a new Item in the ItemRepository.
'''
def test_Item_create(db_connection):
    db_connection.seed("seeds/item_order_seed.sql")
    repository = ItemRepository(db_connection)
    test_item = Item(None, "Webcam", 25.50, 5)
    repository.create(test_item)
    assert repository.all() == [
        Item(1, "TV", 319.99, 4),
        Item(2, "Microwave", 99.99, 10),
        Item(3, "Dishwasher", 450.00, 2),
        Item(4, "Radio", 45.00, 13),
        Item(5, "Webcam", 25.50, 5)
    ]
    assert repository.create(test_item) == None

