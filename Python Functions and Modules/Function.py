# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 16:09:51 2025

@author: ashwi
"""
#Function
#Function are a set of code which,once created,they can be used throughout the program.
#1.Define th function
#2.Call the function

def add():#Defining the function
    x=10
    y=5
    print(x+y)
add()#calling the function

######################################
    
def add( a, b):#Define th function
    print(a+b)
add(10,10)    #Call the function
add(1,1)
add(5,5)

def rect(length,width): #parameter passing
    print("Area of rectangle is::",length*width)
rect(12,2)    #argument declaring

rect(10,5) 
    
################################
#arbitrary attribute using *
#by indexing we can take any name
def hello(*name):
    print("Hello My name is  ",name[2])
hello("Ram","Sham","Harii")    


##################################################
##Return Statement
#Return keyword in python is used to exit a function and return the value of the function 
def hello():
    return("Helloooo")
print(hello())


def add(a,b):
    return("The addition is ",a+b)
print(add(12,2))
    

#############################
#Recursion in python ::
    #Recursion in most commonly used mathematical and Programming concept.
    #In simple words ,recursion means a function can call itself,giving us a benefit of 
    # of looping through data in order to get a result.
    
def hello():
    print("Hello")
    return(hello())
print(hello())    
    

# Factorial Function    
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))    
    
    
    
def fact(n):
    if n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * fact(n - 1)

print(fact(5))

  # 120  


##################################################


###########  Lambda Function   ################
# It is used when an anonymous function is 
   # required for a short period of time.
#It can take numerous arguments.
#It can only have one expression.

a= lambda b:b*5
print(a(5))


x = lambda a,b,c : (a+b)*c
print(x(1,2,3))
    

########################################################
 ######### Local and Global Variable ###########

#Local Variable
x=26
def hello():
    x=25  #local var
    return x
print(hello())




# Global variable
message = "Hello, world!"

def greet():
    # Using the global variable without modification
    print(message)

greet()  # Output: Hello, world!



# Global variable
message = "Hello, world!"

def greet():
    # Local variable shadows the global variable
    message = "Hi there!"
    print(message)

greet()          # Output: Hi there!
print(message)   # Output: Hello, world!



#####################################################
#Practice Questions

# 1. Finding max number.
def max_num(a,b,c):
    if a>=b and a>=c:
        print(a,"is greater")
    elif b>=a and b>=c:
        print(b,"is greater")
    else:
        print(c,"is greater")
print(max_num(12,4,81))


# 2.Write a python function to create and print lits where
#   the values are square of number between 1 to 30.

def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())    

  
# 3. Write a python function that takes a number as a
#    parameter and check if the number is prime or not.

def check_prime(num):
    if num == 1:
        print("Not a prime number.")
    elif num == 2:
        print("Prime number.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("Prime number.")

check_prime(11)
            

# 4. Write a python function to sum all thr numbers in list.

def sum_all_num(list1):
    sum=0
    for i in list1:
        sum+=i
    return sum 

print(sum_all_num([12,3,5,10,5]))    

#solution 2. using recursion

def add(number):
    if len(number) == 1:
        return number[0]
    else:
        return number[0] + add(number[1:])

print(add([12, 5, 5, 13, 0]))



# 5. Find fibonacci Series
#Solution 1:
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))  # Will print: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#solution 2.
def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return (fibonacci(num-1)+fibonacci(num-2))
print(fibonacci(10))    


def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

for i in range(1, 8):  # to print first 7 numbers
    print(fibonacci(i), end=" ")



















