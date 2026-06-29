

#This program calculates the factorial of a number entered by the user.

#A factorial means multiplying a number by all the positive whole numbers below it.
#For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

number = int(input("Enter a number:"))

def factorial(number):
    if number == 0 or number == 1:     #Base case — tells the function when to stop.
        return 1
    else:                              #Recursive case — where the function calls itself.
        return number * factorial(number - 1)
    
result = factorial(number)
print(result)
