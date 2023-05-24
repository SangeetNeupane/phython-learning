a=int(input("Enter the Mark of Science:-"))
b=int(input("Enter the Mark of Math:-"))
c=int(input("Enter the Mark of Social:-"))
d=int(input("Enter the Mark of Economics:-"))
if((a <33)or (b<33) or (c<33) or (d<33)):
    print("You are fail by Subject.")
elif(((a+b+c)/3)<40):
    print("You are pass by Subject and fail by Percentage.")
else:
    print("Congratulations!!! You Are Pass.")