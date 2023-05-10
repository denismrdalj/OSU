fhand = open('LV1/song.txt')
song = []
dicktionary = {}

for line in fhand:
    line = line.rstrip()

    for word in line.split():
        if word.endswith(','):
            word = word.rstrip(word[-1])
        dicktionary[word] = 0
        song.append(word)

fhand.close ()

for word in song:
    dicktionary[word] = dicktionary[word] + 1

print(dicktionary)

for word in dicktionary:
    if dicktionary[word] == 1:
        print(word)
