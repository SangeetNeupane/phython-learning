num=int(input("Enter the number to check the prime or not:  "))
a=num
prime=True
if(num==0 or num==1):
        print("The Number is either Composite nor prime")
        prime=False
else:
    for i in range(2, num):
        if(num%i ==0 and num!=2):
            prime=False
            break

if prime:
     print("The Number is  Prime:-"+str(a))
else:
    print("The Number is Composite :-"+str(a))