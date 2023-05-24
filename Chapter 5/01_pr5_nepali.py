nepali={
    "kitab":"Book",
    "kursi":"Chair",
    "palang":"Bed",
    "jhayl":"Window"
}
print(nepali.keys())
word=input("Enter the Nepali Words to translate in English:\n")
print(f"The English translate of {word} is {nepali.get(word)}")


