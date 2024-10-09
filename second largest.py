num1=(int(input("enter the number:")))
num2=(int(input("enter the number:")))
num3=(int(input("enter the number:")))
largest=max(num1,num2,num3)
smallest=min(num1,num2,num3)
sum=num1+num2+num3-largest-smallest
print(sum)