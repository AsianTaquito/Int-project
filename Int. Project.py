""" I just decided to expand the calculator
# easier than tryna think of something new
# is making a calculator for your hw cheating?
# https://github.com/AsianTaquito/Int-project """
__author__ = "Sebastian Asiatico"

import math

import random

def main():
    """
This is the main function, it controls the program
    """
    print("welcome")
    print("1) Pre-Calc ", end='')
    print("2) Accounting")
    calc_choice = input("What shall i assist you with today? ")
    if calc_choice == '1':
        pre_calc()
    elif calc_choice == '2':
        acc()
    else:
        print("give up")
        project_needs()


# this was just cause im too lazy to do conversions
def pre_calc():
    """
accesses the menu for the calculus calculator 
    """
    print("1) Convert to degrees ", end='')
    print("2) Convert to radians")
    prob = (input("What type of problem do you need help with? "))
    if prob == '1':
        try:
            x = float(input("x = "))
            print(math.degrees(x))
        except ValueError:
            print("not a number")
    elif prob == '2':
        try:
            x = float(input("x = "))
            print(math.radians(x))
        except ValueError:
            print("not a number")


# ill admit there's better ways to do this
# curious to see if I can get it to do all my calc for me

def acc():
    """
accesses the accounting calculator
    """
    print("1) income statement ", end='')
    print("2) depreciation")
    prob = input("what type of problem do you need help with? ")
    if prob == '1':
        income_statement()
    elif prob == '2':
        depreciation()


# this really just double checks me
def income_statement():
    """
checkes numbers on income statement to make sure all adds up
    """
    try:
        expenses = float(input("total expenses = "))
        revenue = float(input("Enter total revenue = "))
        net_income = expenses - revenue
        r_earnings = float(input("Enter begining retained earnings = "))
        bc_stock = float(input("Begining common stock = "))
        issuance = float(input("how much stock was issued:"))
        c_stock = bc_stock - issuance
        dividends = float(input("Dividends = "))
        e_rearnings = r_earnings + net_income - dividends
        liability = float(input("total liabilities = "))
        stock_hequity = c_stock + e_rearnings
        total_assets = float(input("total assests = "))
        assets = liability + stock_hequity
        book_value = assets - liability
        print("your net income is $", format(net_income, "0.2f"), sep='')
        print("your common stock value is $", format(c_stock, "0.2f"), sep='')
        print("your total stock holders equity is $", format(stock_hequity,
                                                             "0.2f"))
        print("your total assets should be $", format(assets, "0.2f"))
        print("your book value is $", format(book_value, "0.2f"))
        if total_assets == assets:
            print("Everything checks all is balanced")
        elif total_assets < assets:
            print("you have less total assets than assets, ", end='')
            print("double check your numbers")
        elif total_assets > assets:
            print("your total assets exceeds your assets")
            print("double check your numbers")
    except ValueError:
        print("i promise you you're broke")


def depreciation():
    """
calculates depreciation 
    """
    try:
        cost = float(input("How much did the item cost?"))
        residual_value = float(input("How much is the residual value? "))
        life = int(input("What is the life span of item? "))
        depreciation_cost = cost - residual_value
        print("1) For straight line")
        print("2) For double rate")
        print("3) For activity based")
        dep_type = int(input("What type of depreciation would you like to use? "))
        if dep_type == 1:
            straightline = depreciation_cost / life
            print("The yearly depreciation expense is", straightline)
        elif dep_type == 2:
            """ pass """
            # for x in range(life):
            # should calculate it for however many times life =
            # doubleRate()
            # need to def/make this into as chart
            # will come back to fix this hole
        elif dep_type == 3:
            unit_life = int(input("What is the life based on activity/ units? "))
            yearly_activity = int(input("Enter activity for current year: "))
            depreciation_rate = depreciation_cost / unit_life
            expense = yearly_activity * depreciation_rate
            print("The depreciation rate is", depreciation_rate)
            print("And the yearly depreciation expense is", expense)
    except ValueError:
        pass


# don't know if I still need this but just in case
def project_needs():
    """
This covers anything needed for the project that was left out
    """
    try:
        num_1 = float(input("Give me a number: "))
        num_2 = float(input("Give me a number: "))
    except ValueError:
        num_1 = random.randint(0,100)
        num_2 = random.randint(0,100)
        for x in range(num_1 >= 99.9 and num_2 <= 99.9):
            num_1 *= 0
        print(num_1 ** num_2)
        print(num_1 % num_2)
        print(num_1 // num_2)
        print(("G" + "G ") * 52)


again = True
while again:
    main()
    another = input("Enter Y to go again or any of key to end ")
    if another.upper() != 'Y':
        again = False
        print("goodbye")
