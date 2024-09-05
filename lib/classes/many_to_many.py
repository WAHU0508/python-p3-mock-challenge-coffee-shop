class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the coffee name once it has been set.")
        if not isinstance(name, str):
            raise TypeError("Coffee name must be of string type.")
        if len(name) < 3:
            raise ValueError("Customer name should not be less than 3 characters.")
        self._name = name
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be of string type.")
        if not 1<= len(name) <= 15:
            raise ValueError("Customer name characters not between 1 and 15.")
        self._name = name
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

