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






class Refund(Item):
    def __init__(self, id, name, price,amount,reason,product,customerName):
        super().__init__(id, name, price)
       
        self.amount = amount
        self.reason = reason
        self.product = product
        self.Name= customerName

    def informationl_user(self):
        return(f"Our customer {self.Name}  need a refund of her {self.product} because of {self.reason} which he bought at {self.amount}")

    # we need to check if the customer has entered the same amount she/he had paid

    def check_amount(self):
        if self.price == self.amount:
            return(f"The amount is the same")
        else:
            return(f"it doesn't match")

#    when the customer click submit button

    def sent_message(self):
        return(f"Message sent:Refund request for {self.product} by {self.Name} due to {self.reason} with the {self.id} as id of the product")

item1 = Item(1, "Item 1", 10.99)
item2 = Item(2, "Item 2", 5.99)


cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)

print("Items in the cart:")
for item in cart.items:
    print(item.name)

print("Total price:", cart.checkout())       


refund=Refund(1, "Item 3", 10.99, 222,"it's rotten", "apple","Agnes")
print(refund.informationl_user())
print(refund.check_amount())
print(refund.sent_message())

