

# Python program to check whether a number is divisible by both 3 and 5:

# Input from user
number = int(input("Enter a number: "))

# Check divisibility
if number %3 == 0 and number % 5 ==0:  # % is the modulus operator
                                       # It gives the remainder after division
                                       # 10 divided by 3 equals 3 remainder 1 so: 10 % 3 = 1
    print(" The number is divisible by both 3 and 5")
else:
    print("The number is NOT divisible by both 3 and 5.")

# Check divisibility
if number %2 == 0:                     # % is the modulus operator
                                       # It gives the remainder after division
                                       # 10 divided by 2 equals 5 remainder 0 so: 10 % 5 = 2
    print(" The number is divisible by 2")
else:
    print("The number is NOT divisible by 2.")
