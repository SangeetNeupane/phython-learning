num=int(input("Enter the Last Natural Number:-"))
def r_sum(a):
    if a<= 1:
       return a
    else:
        return r_sum(a-1)+a



y=r_sum(num)
print(y)