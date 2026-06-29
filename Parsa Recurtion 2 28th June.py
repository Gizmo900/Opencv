
#This Python program asks the user how many natural numbers they want to add together, 
# then calculates the sum from 1 up to that number using recursion.

# Recursion in Python means a function calls itself to solve a problem step by step.
#A recursive function needs two important parts:

              #Base case — tells the function when to stop.
              #Recursive case — where the function calls itself.

number = int(input("How many natural numbers do you want to calculate the sum?"))

def sum_numbers(number):
    if number == 0: # base case
        return 0
    else:
        return number + sum_numbers(number - 1) # recursive case
    
result = sum_numbers(number)
print(result)