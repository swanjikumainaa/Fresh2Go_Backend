class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                break

    def checkout(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        self.items = []
        return total_price
item1 = Item(1, "Item 1", 10.99)
item2 = Item(2, "Item 2", 5.99)

cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)

print("Items in the cart:")
for item in cart.items:
    print(item.name)

print("Total price:", cart.checkout())
