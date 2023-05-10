"""l = [5, 3, 8, 10, 2, 7]
x = int(input('Лічба ?'))

def find():
    a = len(l)
    b = l.pop(int((a - 1) / 2))
    while b != x:
        a = a / 2
        b = l.pop(int((a - 1) / 2))
    print(b)

find()

"""
from random import randint

a = randint(1, 100)
top = 100
low = 1
mid = 0

while mid != a:
    mid = int((top + low) / 2)
    print('верх', top)
    print('ніз', low)
    
    print('сярэдіна', mid)
    if mid > a:
        top = mid
    else:
        low = mid