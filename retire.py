# Retirement calculator 
# Input the you name and age and the program will tell you when you can retire

import datetime 
now = datetime.datetime.now()
Current_year = now.year


# Current_year = 2019

Retirement_age = 66

print("Retirement Calculator")
name = input("What is your name? ")

age = input("What is your a Age? ")

retirement = 66 - int(age) + Current_year 
print(name + ", you can retire in " + str(retirement))

# # Part 2 - Let's get rich
# # Compound interest formula is:  P(1 + R/100)r

principle = float(input("How much money do you have now: "))
rate = float(input("Enter the current interest rate: "))
time = float(66 - int(age))

money = principle * (pow((1 + rate / 100), time))

print(name + ",when you retire in " + str(retirement) + "you will have" + str(money) + "in the bank" )

print("{0}, when you retire in {1} you will have ${2:,.2f} in the bank".format(name,retirement,money))

# Python > 3.6
# If you are not using > 3.6 this will crash -- use shift comand(ctrl) p and select Python
# 

print(f"{name}, when you retire in {retirement} you will have ${money:,.2f} in the bank! ")