a=input("Enter the text:")
if("make a lot money"in a):
    spam=True
elif("buy now"in a):
    spam=True
elif("subscribe this"in a):
    spam=True
elif("click this"in a):
    spam=True
else:
    spam=False

if(spam is True):
    print("This text is Spam.")
else:
    print("This text is not Spam.")