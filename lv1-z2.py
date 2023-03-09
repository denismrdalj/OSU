x = 99
while x < 0 or x > 1:
    print('Unos ocjene: ')
    try:
        x = float(input())
    except:
        int('Invalid input, must be float [0.0, 1.0]')
    else:
        if x > 0 or x < 1:
            break
        else:
            print('Out of range')
            


if x > 0.0 and x < 1.0:
    if x < 0.6:
        print('F')
    if x >= 0.6 and x < 0.7:
        print('D')
    if x >= 0.7 and x < 0.8:
        print('C')
    if x >= 0.8 and x < 0.9:
        print('B')
    if x >= 0.9:
        print('A')
