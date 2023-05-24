a="my name is  sangeet"
b=a.find("  ")
if(b>=0):
    print("Double Space Detected.")
else:
    print("Double Space not Detected.")

a=a.replace("  "," ")
print(a)
b=a.find("  ")
if(b>=0):
    print("Double Space Detected.")
else:
    print("Double Space not Detected.")
