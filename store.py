class Product:
    def __init__(self,name,price,upc):
        self.name = name
        self.price = price
        self.upc = upc
    def __add__(self,other):
        return self.price+other.price

class Container:
    type_of_con = 'Bottle'
    def set_size_of_bottle(self,size):
        self.bottle_size = size


class Detergent(Product,Container):
    product_category = "Soap"

    def set_price(self, price):
        self.bot_price = price
    def __len__(self):
        return 300

class Soap(Product):
    def set_price(self,price):
        self.price_of_bar = price
    def __len__(self):
        return 500
s = Detergent('Private',100,239048908)
s.set_size_of_bottle(200)
#s.set_price(100)

f = Soap('Lux',80,8923798)
s.set_price(100)
f.set_price(200)
print s.name,s.price,s.upc,s.product_category,s.type_of_con,s.bot_price
print f.price,f.name,f.upc,f.price_of_bar

print len(s),len(f)

print s+f
print s.__add__(f)