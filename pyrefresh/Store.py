class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({ 
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        return sum([item['price'] for item in self.items])
#        for item in self.items:
#            total += item['price']
#        return total

    def display_stock(self):
        print(self.items)

    @classmethod
    def franchise(cls, store):
        return cls("{} - franchise".format(store))
        
    @staticmethod
    def store_details(store):
        print("{}, total stock price: {}".format(store.name, store.stock_price()))



#maks = Store("Maks")
#maks.add_item("C4 Rubber", 22)
#maks.add_item("Petzel Harness", 64)
#maks.add_item("ATC", 24)
#maks.add_item("Rope", 137)
#maks.display_stock()
#print(maks.stock_price())

store = Store("Vons")
store2 = Store("Keils")
store2.add_item("Kale", 3.98)
store2.add_item("Banana", 4.98)

store3 = Store.franchise(store)
Store.franchise(store2)

print(type(store))
print(type(store2))

Store.store_details(store)
Store.store_details(store2)
Store.store_details(store3)

