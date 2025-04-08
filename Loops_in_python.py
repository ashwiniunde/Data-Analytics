# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:19:19 2025

@author: ashwi

"""
#Nested Loop::

for i in range(1,4):#rows count
    for j in range(11):#columns count 
        print(j,end=" ")
    print()    
"""
OUTPUT::
    0 1 2 3 4 5 6 7 8 9 10 
    0 1 2 3 4 5 6 7 8 9 10 
    0 1 2 3 4 5 6 7 8 9 10 
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
OUTPUT:
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j ,end=" ")
    print() 
"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
"""    
    
##For loop with conditional statements
for i in range(1,11):
    if i==3:
        print("Hii")
    else:
        print(i)
         
"""  
OUTPUT::
    1
    2
    Hii
    4
    5
    6
    7
    8
    9
    10
"""   
  

for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)
"""
OUTPUT::
    24
    48
    72
    96
"""

n=1
while n <=10:
    if n==3:
        print("Three")
    else:
        print(n)
    n+=1    
"""
OUTPUT::
    1
    2
    Three
    4
    5
    6
    7
    8
    9
    10
"""    
#####################################
###Problem solving
#1.Sum of all even number upto 50
sum=0
for i in range(0,51):
    if i%2==0:
        sum=sum+i
print("Sum of all even number upto 50::::",sum)    
    
#2. Write a program to write first 20 numbers and their squared numbers..
for i in range(1,21):
    print(i,"==",i*i)
    
#3.Write a program to find sum of first 10 odd numbers and their using while loop.

n=0
sum1=0
while n<20:
    if n%2!=0:
        sum1+=n
    n+=1
print("Sum of odd number upto 20:::",sum1)
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    