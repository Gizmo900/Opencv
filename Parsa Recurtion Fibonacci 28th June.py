


# This program calculates the Fibonacci sequence using recursion.
#The Fibonacci sequence is:

#0, 1, 1, 2, 3, 5, 8, 13, ...
# Recursion in Python means a function calls itself to solve a problem step by step.
#A recursive function needs two important parts:

              #Base case — tells the function when to stop.
              #Recursive case — where the function calls itself.

n = int(input("Enter the number of terms for the Fibonacci sequence:"))

def fibonacci(n):
    if n<=1:             #Base case — tells the function when to stop.
        return n
    else:                  #Recursive case — where the function calls itself.
        return fibonacci(n - 1)+ fibonacci(n - 2)
    
for i in range(n):
    print (fibonacci(i))