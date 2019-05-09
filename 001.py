import string
import random
# import sys
# sys.setrecursionlimit(1000000)

m = string.ascii_letters + string.digits

def get_key():
    key = ''
    for i in range(1 ,10):
        key += random.choice(m)
        if i % 3 == 0 and i != 9:
            key += '-'
    return key

def show_key():
    tmp = []
    for i in range(200):
        one_key = get_key()
        if one_key not in tmp:
            tmp.append(one_key)
    for key in tmp:
        with open('002.txt', 'a+') as f:
            f.write(key+' ')

if __name__ == '__main__':
    show_key()