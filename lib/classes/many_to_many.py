class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the coffee name once it has been set.")
        if not isinstance(value, str):
            raise TypeError("Coffee name must be of type str.")
        if len(value) < 3:
            raise ValueError("Customer name should be at least 3 characters long.")
        self._name = value
    def orders(self):
        return self._orders
    
    def customers(self):
        return list({order.customer for order in self._orders if isinstance(order.customer, Customer)})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all.append(self)
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
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders if isinstance(order.coffee, Coffee)})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer should be an instance of Customer class.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee should be an instance of Coffee class.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee._orders.append(self)
        customer._orders.append(self)
        Order.all.append(self)
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be of float type.")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change after the order is instantiated.")
        self._price = value
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee

latte = Coffee("Latte")
print(latte.name)
customer1 = Customer("Wahu")
print(customer1.name)
order1 = Order(customer1, latte, 1.50)
print(latte.orders())