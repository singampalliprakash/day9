#using factorial function
import math
num=int(input("enter the number:"))
factorial=math.factorial(num)
print("the factorial of the number is",num,"is",factorial)
#using for loop
n=int(input("enter the number:"))
factorial=1
if n>=1:
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"the factorial of the number:{factorial}")
#using recursion
def recursion_factorial(n):
    if n==1:
        return n
    else:
        return n*recursion_factorial(n-1)
if n < 0:
    print("factorial does not exist")
elif n==1:
    print("the factorial of n is 1")
else:
    print("the recurison of ",n,"is",recursion_factorial(n))



    


