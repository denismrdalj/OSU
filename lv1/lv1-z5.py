fhand = open('SMSSpamCollection.txt', encoding="utf8")

spam = 0
ham = 0
z = 0
messages = 0
for line in fhand:
    messages+=1
    if line.strip().endswith('!'):
        print("USKLIČNIK")
        z+=1
    if line.startswith('spam'):
        spam+=1
    if line.startswith('ham'):
        ham+=1

        
print("Prosječan broj spam poruka:")
print(float(spam/messages))

print("Prosječan broj ham poruka:")
print(float(ham/messages))

print("Broj poruka koje završavaju s uskličnikom")
print(z)
fhand.close()
