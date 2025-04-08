# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 16:07:53 2025

@author: ashwi
"""

### Python Basics - Jupyter Notebook

# Introduction to Python for Data Analytics
"""
Python is a versatile programming language widely used in data analytics, machine learning, and web development.
It provides powerful libraries like NumPy, Pandas, and Matplotlib for data processing and visualization.
"""

# First Program in Python
print("Hello, World!")

# Comments, Variables, Datatypes, User-Inputs
# Single-line comment
""" Multi-line comment """
name = input("Enter your name: ")  # Taking user input
age = 25  # Integer variable
gpa = 3.8  # Float variable
is_student = True  # Boolean variable
print(f"Hello {name}, you are {age} years old.")



# TypeCasting, Subtypes, Problem-Solving
num_str = "100"
num_int = int(num_str)  # Typecasting string to integer
num_float = float(num_int)  # Typecasting integer to float
print(num_float)



# Operators and Operands
x, y = 10, 5
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
power = x ** y
print(addition, subtraction, multiplication, division, modulus, power)

# Conditional Statements
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
