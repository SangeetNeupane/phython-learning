num=int(input("Enter the number to Factorial:  "))
a=1
fact =1
for i in range(0,num):
    fact=fact*a
    a=a+1

print(str(fact))