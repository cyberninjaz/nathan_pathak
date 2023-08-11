import random

class hungrypeople:
    def __init__(self, buns, dogs, toppings, price, name, time):
        self.buns = buns
        self.dogs = dogs
        self.toppings = toppings
        self.price = price
        self.name = name
        self.time = time

    def get_order(self):
        return [self.buns, self.dogs, self.toppings]
    
    def time_limit(self):
        return self.time
    
    def the_price(self):
        return self.price

def customers():

    doglist = ['Vegan dog', 'Beef dog', 'Chicken dog', 'Nathans hotdogs dog']

    bunslist = ['White bun', 'Whole wheat bun', 'Gluten free bun', 'Pretzel bun', 'Crispy bun']

    toppingslist = ['Ketchup', 'Mustard', 'Lettuce', 'Mayo', 'Peppers and Onion', 'Chili Cheese']

    timelist = [20, 25, 18, 28]

    namelist = ['Karen', 'Bob from walmart', 'Joey', 'Sarah', 'Creature', 'George', 'Taylor', 'Maya', 'Joesephine', 'Adrian', 'Mae', 'Joy']

    pricelist = [10, 8, 6]

    customerlist = []

    for x in range(20):
        customerlist.append(hungrypeople(random.choice(bunslist), random.choice(doglist), random.choice(toppingslist), random.choice(pricelist), random.choice(namelist), random.choice(timelist)))

    return customerlist

def checking(customer_list, your_hotdog):
    
    countfun = 0
    
    for item in customer_list:

        if item == your_hotdog[countfun]:
            pass

        else:
            return False
        
        countfun += 1

    return True