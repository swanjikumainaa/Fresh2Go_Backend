
# first method

def search_func(products, product):
    if not products:    # shorter way to test if the list is empty
        return "failure"
    for x in products: 
        if x == product: 
            return "success"
    else:
        return "failure" 
my_list = ["banana", "avocado", "carrots", "peas"]
prduct = "avocado"
index = search_func(my_list, prduct)
print(index) 


# second method

class DictionarySearch:
    def __init__(self, products):
        self.products = products

    def search_product(self, key, value):
        for product, amount in self.products.items():
            if product == key and amount == value:
                return (product, amount)
        return None
    

my_products = {'banana': 5, 'avocados': 6, 'peas': 9}
search = DictionarySearch(my_products)

result = search.search_product('peas', 9)
if result:
    print(f"({result[0]}, {result[1]}) is available")
else:
    print("product not found.")







