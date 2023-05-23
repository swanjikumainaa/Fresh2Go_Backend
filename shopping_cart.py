class Item:
    def __init__(self, id, name, price, discount):
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
    # Add get methods for Item properties
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_discount(self):
        return self.discount
class ShoppingCart:
    def __init__(self):
        self.items = []
# add item to cart
    def add_item(self, item):
        self.items.append(item)
#remove item from cart
    def remove_item(self, item_id):
        for item in self.items:
            if item.get_id() == item_id:
                return self.items.remove(item)
# checkout cart and add discount if any
    def checkout(self):
        total_price = 0
        for item in self.items:
            if item.get_discount() > 0:
                # takes in discount in % and subtracts it from the total price
                total_price += (item.get_price() * (1 - item.get_discount()/100))
            else:
                total_price += item.get_price()
        self.items = []
        return total_price
item1 = Item(1, "Item 1", 100.00, 10)
item2 = Item(2, "Item 2", 200.00, 10)
cart = ShoppingCart()
# add item to the cart
cart.add_item(item1)
cart.add_item(item2)
# checkout cart
print(cart.checkout())
