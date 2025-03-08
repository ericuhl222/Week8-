#Eric Uhl
#2.17.25
#computer science
#i will succeed!

import random

def purchase_item(item_price, starting_money, quantity):
    total_purchase = (item_price * quantity)
    if starting_money < total_purchase:
        quantity = quantity - 1
        total_purchase = (item_price * quantity)
        if starting_money < total_purchase:
            quantity = quantity - 1
        if starting_money > total_purchase:
            leftover_money = starting_money - (item_price * quantity)
            starting_money
            return(quantity, leftover_money)
            #this portion is to ensure the code doesnt buy more than it can afford.
    if starting_money > total_purchase:
        leftover_money = starting_money - (item_price * quantity)
        starting_money
        return(quantity, leftover_money)
        



purchase_item ((random.random()), random.randint(1,6), random.randint(0,4))
purchase_item ((random.random()), random.randint(1,6), random.randint(0,4))
purchase_item ((random.random()), random.randint(1,6), random.randint(0,4))

#second monster code.

def new_random_monster():
    monsters = ["demon", "ghost", "goblin", "creeper"]
    health = random.randint(0,185)
    money = random.randint(0,185)
    power = random.randint(1,5)
    sel_health = health * power
    sel_monster = random.choice(monsters)

    scenario = [(f'You come across a {sel_monster} eating a corpse'), (f"A {sel_monster} jumps out from beind a crate"), (f'After entering a cave a {sel_monster} attacks you from a dark corner')]
    sel_scenario = random.choice(scenario)
                                                                   
    return(sel_health, money, sel_monster, sel_scenario)

#fuction for monster
new_random_monster()
new_random_monster()
new_random_monster()


#takes name as arg returns "hello name!"

def print_welcome(name):
    text = (f"Hello {name}")
    centered_text = text.center(15)
    print(centered_text)

name = input()
print_welcome(name)

#Prints a menu for a shop

def print_shop_menu(item1, x: float, item2, y: float):
    print('/' + '-' * 22 + '\\' )
    print(f"|{item1:<15}{x:>7}|",)
    print(f"|{item2:<15}{y:>7}|",)
    print('\\' + '-' * 22 + '/' )

    #fuction for shop =D
print_shop_menu('milk', 14.99, 'pie', 18.48)


