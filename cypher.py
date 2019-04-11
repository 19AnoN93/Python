def cypher(original, key, keystring):
    cyphedText = ""
    for l in original:
        num = findNum(l, keystring)
        num = num + key
        num = num % len(keystring)
        cyphedText = cyphedText + keystring[num]
    return cyphedText
    
def findNum(l, keystring):
    return keystring.find(l)
    
original = input("Write your text: ")
key = int(input("Write key of cypher(correct number): ")) #cypher - шифрование
keystring = "абвгдеёжзийклмнопрстуфхцчшшщъыьэюяАБВГДЁЖЗИЙКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ"
a = input("desypher or sypher? d or s: ")


if a == "d":
    key = -key
elif a == "s":
    pass
else:
    print("OPREDELYS!")
cyphedText = cypher(original, key, keystring)
print("\nThe text " + original + " now " + cyphedText)
