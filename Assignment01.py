# -*- coding: utf-8 -*-

'''
#Challenge 1: Temperature conversion
print("Temperature conversion.")
user_input = int(input("Please select an option: "))
if user_input == 1:
    print("Conversion from degrees Fahrenheit to Celsius.")
    F = float(input("Enter a temperature value in Fahrenheit: "))
    C = 5/9 * (F - 32)
    print(f"{F} degrees Fahrenheit are {C} degrees Celsius.")
elif user_input == 2:
    print("Conversion from degrees Fahrenheit to Kelvin.")
    F = float(input("Enter a temperature value in Fahrenheit: "))
    K = (5/9 * (F - 32)) + 273.15
    print(f"{F} degrees Fahrenheit are {K} degrees Kelvin.")
else:
    print("Invalid option.")
'''

'''
# Challenge 2: Voltage division
print("Voltage output calculator.")
V_in = float(input("Enter the input voltage (Vin) value: "))
R1 = float(input("Enter Resistor 1 (R1) value in ohms: "))
R2 = float(input("Enter Resistor 2 (R2) value in ohms: "))
V_out = (R2/(R1 + R2)) * V_in
print(f"The voltage outpu is {V_out} Volts.")
'''

'''
#Challenge 3: 3 and 7 FizzBuzz
print(" 3 and 7 FizzBuzz")
N = int(input("Enter a number: "))
for i in range(1, N+1):
    if i % 3 == 0 and i % 7 != 0:
        print(f"{i}: Fizz")
    elif i % 7 == 0 and i % 3 !=0:
        print(f"{i}: Buzz")
    elif i % 3 == 0 and i % 7 == 0:
        print(f"{i}: FizzBuzz")
    else:
        print(i)
'''


'''
#Challenge 4: Kiosk machine 
print("Welcome to McBurger Queen.") 
subtotal = 0 
while True:
    user_selection = int(input("Please, select an option from the menu: "))
    if user_selection == 1:
        print("McWhopper added.")
        subtotal += 6.89
    elif user_selection == 2:
        print("Crispy McFish added.")
        subtotal += 4.99
    elif user_selection == 3:
        print("Fries added.")
        size = input("Please select the size: ")
        if size == 'a':
            print("Small")
            subtotal += 0.99
        elif size == 'b':
            print("Medium")
            subtotal += 1.99
        elif size == 'c':
            print("Large")
            subtotal += 2.99
    elif user_selection == 4:
        print("Soda added.")
        size = input("Please select the size: ")
        if size == 'a':
            print("Small")
            subtotal += 0.50
        elif size == 'b':
            print("Medium")
            subtotal += 1.50
        elif size == 'c':
            print("Large")
            subtotal += 2.00
    elif user_selection == 5:
        print("Happy Meal added")
        subtotal += 6.99
    elif user_selection == 6:
        print("Family Deal added")
        subtotal += 19.99
    elif user_selection == 7:
        print(f"Your subtotal is ${subtotal}.")
        sales_tax = (0.08875 * subtotal)
        print(f"The total tax amount is ${sales_tax}.")
        total = subtotal + sales_tax
        print(f"Your total amount is ${total}.")
        print("Thank you for shopping at McBurger Queen. Have a nice one!")
        break     
    else:
        print("Invalid option, please pick again!")
'''

'''
#Challenge 5: Day of the programmer
print("When is the programmer's day? ")
year = int(input("Enter a year: "))
if year <= 1700 or year >= 2700:
    print(f"The {year} is an invalid year. Pick another year between 1700-2700")    
elif year == 1918:
    print(f"In the {year}, the day of the programer is 09.26")
elif year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print(f"In the {year}, the day of the programer is 09.12")
else:
    print(f"In the {year}, the day of the programer is 09.13")
'''  

   

    





























