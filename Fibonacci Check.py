# A program to check if a number if a fibonacci number or not.

# The function
def fib(x):

    a = 0
    b = 1

# Checking if the value entered is on of the first two fibonacci numbers
    if x == 0 or x == 1:
        print(x, "is a fibonacci number.")

# Assigning the value of the third fibonacci number to c

    c = a+b

# Checking fibonacci values to the value provide (x)
    while c < x:
        a = b
        b = c
        c = a + b

# Checking if x is any of the fibonacci numbers or not
    if c == x:
        print(x, "is a fibonacci number.")
    else:
        print(x, " is not a fibonacci number.")

# Prompt to ask user for the number to test if fibonacci or not

print("This is a program that checks if a number if fibonacci or not.")
x = int(input("Enter the number to be tested: "))

# calling the function

fib(x)