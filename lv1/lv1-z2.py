try:
    percentage = -1.0
    while percentage < 0.0 or percentage > 1.0:
        percentage = float(input('Enter percentage: '))

    if percentage >= 0.9:
        print('A')
    elif percentage >= 0.8:
        print('B')
    elif percentage >= 0.7:
        print('C')
    elif percentage >= 0.6:
        print('D')
    elif percentage < 0.6:
        print('F')
except:
    print('You need to enter a number')

