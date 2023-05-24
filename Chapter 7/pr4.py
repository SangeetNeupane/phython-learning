num=int(input("Enter the number to check the prime or not:  "))
a=num
if(num==0 or num==1):
        print("The Number is either Composite nor prime")
else:
    for i in range(1, num):
        i=i+1
        if(num%i ==0 and num!=2):
            print("The Number is Composite :-"+str(a))
            break
        else:
            print("The Number is  Prime:-"+str(a))
            break
