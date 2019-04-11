a = "__________5___________"
print(a)
a = a.rstrip('___')
print(a)

print(" ")

b = "Мама мыла раму xD"
print(b)
b = b.replace('раму', 'папу', 1)
print(b)
b = b.replace('мыла', 'била', 1)
print(b)

print(" ")

c = "мама мыла раму"
c = c.upper()
c = c.split()
for i in c:
    print(i)
