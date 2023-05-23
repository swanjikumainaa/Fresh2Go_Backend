
# searching for a product engine

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


