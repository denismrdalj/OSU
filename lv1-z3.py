import warnings

def avg(list):
    print('Average: ', sum(list)/len(list))

def min(list):
    list.sort()
    print('Min: ', list[0])

def max(list):
    list.sort()
    list.reverse()
    print('Max: ', list[0])

list = []
counter = 0
while True:
        print('Unos ocjene= ')
        x=input()
        if not x.isdigit():
            if x == 'Done':
                break
            else:
                warnings.warn('Invalid input ignored.')
        if x.isdigit():
            list.append(int(x))
            counter+=1



print('\nCount: ',counter)
avg(list)
min(list)
max(list)
list.sort()
print('Sorted: ',*list, sep=', ')


