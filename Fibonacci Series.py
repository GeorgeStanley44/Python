
# The function
def fib(n):
    a=0
    b=1
    if n==1:
        print (a)
    else:
        print (a)
        print (b)
        for i in range (2,n):
            c = a+b
            a = b
            b = c
            print(c)

# Program to get fibonacci sequence

n = int(input("Enter the number of terms(as an integer): "))
if n <= 0:
    print("Enter a positive integer")
else:
    fib(n)