not_alfabet = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'q', 'r', 's', 'v', 'w', 'x', 'y', 'z']


def detector(l):
    global not_alfabet
    l = l.lower()
    for i in not_alfabet:
        if i in l:
            return 'NO'
    if l[0:3] == 'put' and l[0:5] != 'puton':
        return 'NO'
    l = l.replace('one', ' ')
    if 'e' in l:
        return 'NO'
    l = l.replace('puton', ' ')
    if 'on' in l:
        return 'NO'
    if ' p' in l:
        return 'NO'
    l = l.replace('in', ' ')
    l = l.replace('out', ' ')
    if ('i' in l) or ('o' in l) or ('n' in l):
        return 'NO'
    for i in ['p', 'u', 't']:
        if 'put' + i in l:
            return 'NO'
    l = l.replace('put', ' ')
    if not l.isspace():
        return 'NO'
    return 'YES'


N = int(input())
l = []
for i in range(N):
    l.append(input())

for i in l:
    print(detector(i))
