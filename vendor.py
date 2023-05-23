class vendor:
    def __init__(self,name,location,contact):
        self.name=name
        self.location=location
        self.contact=contact
        self.inventory = {}
        self.products = []
    def add_product(self, product):
        self.products.append(product) 
    def update_inventory(self, product, quantity):
        self.inventory[product] = quantity      

vendor1= vendor("Mary","Kilimali","+254345675")  
vendor1.add_product("apples")   
print(vendor1.products)
vendor1.update_inventory("Mangoes",5)
print(vendor1.inventory)

    

