a=input("Enter Your Name:-")
b=input("Enter the Date:-")
letter='''Dear Name,
You are Selected
Date'''
letter=letter.replace("Name",a)
letter=letter.replace("Date",b)
print(letter)
