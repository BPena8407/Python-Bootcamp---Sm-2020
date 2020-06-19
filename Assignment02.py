# -*- coding: utf-8 -*-

# Assignment 02

# PART I

# PC # 1: The odd list

'''
def some_function(some_list):
    another_list = []
    for i in some_list:
        if i % 2 == 1:
            another_list.append(i)
    outcome = another_list
    return outcome

cute_list = [1, 2, 5, 3, 8, 9]
outcome = some_function(cute_list)
print(outcome)
'''

# PC #2: Multiples

'''
def a_function(N):
    another_list1 = []
    for number in range(0, 100):
        if number % N == 0:
            another_list1.append(number)
    outcome1 = another_list1
    return outcome1

outcome1 = a_function(12)
print(outcome1)
'''

# PC #3: Sorted or not

'''
def a_third_function(a_list):
    a_second_list = a_list[:]
    a_second_list.sort()
    if a_list == a_second_list:
        print("The list is in ascending order.")
    else:
        print("The list is not in ascending order.")


my_list = [1, 3.0, 2, 1.5]
outcome2 = a_third_function(my_list)

my_list1 = [1, 3, 5, 7, 9]
outcome3 = a_third_function(my_list1)
'''

# PC #4: Slot machine

'''
import random

possible_outcome = ['Cherry', '7', 'J', '10', 'Apple', 'A', "Q", 'M']  
def slot_machine(possible_outcome):
    lucky_list = []
    i = 0
    while i < 3:
        lucky_list.append(random.choice(possible_outcome))
        outcome4 = lucky_list
        i += 1
    return(lucky_list)

Result = slot_machine(possible_outcome)
print(Result)
'''

# PART III - Chemical Engineering major

# PC #1: Charle's Law

#Temperature given in Celsius

'''
def v_final(Tin, Vin, Tout):
    V_out = (Vin * (Tout  + 273.15))/(Tin + 273.15)
    return V_out

result = v_final(0, 8.57, 82)
print(f"The final volume equals {result} L.")
'''

# (That was very fun to try)


# PC #2: Average atomic mass

'''
def avg_AM(A_masses, Fract_a):
    average_atomic_mass = 0
    for i in range(len(A_masses)):
        average_atomic_mass += A_masses[i] * Fract_a[i]
    return average_atomic_mass
    
    
a_mass = [34.9689, 36.9659]
f_abs = [0.75711, 0.24229]
Result = avg_AM(a_mass, f_abs)
print(Result)
'''
    
# This is one of the many codes that did no work for this question 
# why is it not working?   

''' 
def avg_AM(A_masses, Fract_a):   
    atom_mass = []
    for i, j in zip(A_masses, Fract_a):
        atom_mass.append(i * j)
        average_atomic_mass = 0
        for k in atom_mass:
            average_atomic_mass += atom_mass[k]
    return average_atomic_mass

a_mass = [1, 2, 3, 4, 5]
f_abs = [2, 4, 6, 8, 10]
Result = avg_AM(a_mass, f_abs)
print(Result)
'''  
      
 # I found this question specially challenging, 
 # I needed a lot of help to complete it 
    
 