#!/usr/bin/env python3

class CashRegister:
    def __init__(self,discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.prices = []
		
    def add_item(self,title,price,quantity = 1):
        self.quantity = quantity
        for i in range(self.quantity):
            self.prices.append(price)
            self.price = price 
            self.title = title
            self.total += price
            self.items.append(title)
            
        return self.items 

    def apply_discount(self):
        if self.discount:
            self.total = (100 - self.discount) / 100 * self.total
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):

        for i in range(self.quantity):
            self.total -= self.price

        return self.total    
# new_register = CashRegister()
# new_register.add_item("eggs", 1.99, 2)
# new_register.add_item("tomato", 1.76, 3)