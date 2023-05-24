a=int(input("Enter the Number 1:-"))
b=int(input("Enter the Number 2:-"))
c=int(input("Enter the Number 3:-"))
d=int(input("Enter the Number 4:-"))

if(a>b):
    num=a
else:
    num=b

if(c>d):
    num1=c
else:
    num1=d

if(num>num1):
    print(f"The greatest number among four is {num}")
else:
    print(f"The greatest number among four is {num1}")
