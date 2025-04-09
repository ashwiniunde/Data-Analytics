# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 22:13:44 2025

@author: ashwi
"""
## Modules :
"""
Modules are the (.py) files that 
contains set of functions you
want to include in your program
"""

# In-built modules in python

###### 1.DateTime ##########
import datetime
x=datetime.datetime.now()
x

y=datetime.datetime(2022,11,11)
y
y.strftime("%A") #'Friday'

y.strftime("%a") #'Fri'

y.strftime("%m") #'11'

y.strftime("%B")  #'November'

y.strftime("%Y")  # '2022'

y.strftime("%y") #'22'

y.strftime("%d")    #'11'


###############################################################
######### 2. Random Module  #######
# Generate random numbers (integers or floats)


import random

x = random.randint(1, 10)  # Random integer from 1 to 10
print(x)

l = ["Heads", "Tails"]  # Coin sides
x = random.choice(l)  # Randomly pick one
print(x)


#Random Quiz Question Picker
import random

questions = ["What is AI?", "Explain OOP.", "What is a database?", "Define recursion."]
q = random.choice(questions)
print("Your question is:", q)


######################################
import random

questions = ["Q1", "Q2", "Q3", "Q4"]
random.shuffle(questions)

print("Today's quiz questions:")
for q in questions:
    print(q)

###############################
#Roll a Dice
import random

dice = random.randint(1, 6)  # Simulates a 6-sided dice
print("You rolled:", dice)

#################################
# Lucky Draw Winner
import random

participants = ["Ashwini", "Yuki", "Ken", "Mina", "Ryo"]
winner = random.choice(participants)
print("And the winner is... 🎉", winner)


#################################################################
####### 3. math module ######
import math

x=max(12,45,23)
print("The maximum value is",x) #The maximum value is 45


x=min(12,45,23)
print("The minimum value is",x) #The minimum value is 12


a=pow(5,2)
print(a) #25


b=math.sqrt(25)
b  # 5.0


c=abs(-12)
c # 12
 
c=abs(-12.56)
c # 12

k= math.ceil(2.4) #next closest num
print(k) # 3

m=math.floor(2.4) #previous closest number
print(m)   # 2











