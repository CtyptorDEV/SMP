def bubble(s):
    flag = True
    while flag:
        flag = False
        for i in range(len(s)-1):
            if s[i+1] < s[i]:
                s[i+1], s[i] = s[i], s[i+1]
                flag = True
    return s
def pops(s):
    flag = True
    while flag:
        flag = False
        for i in range(len(s)-1):
            if s[i][0] == s[i+1][0]:
                if s[i] == []:
                    continue
                elif s[i+1][1] >= s[i][1]:
                    s[i] = [0]
                else:
                    s[i+1] = [0]
                flag = True
    return s
def delete(s):
    if s[i] == [0]:
        s.pop(i)
    return s


l = []
s = []

n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    l.append(a)
    l.append(b)
    l.append(i+1)
    s.append(l)
    # print(s)
    l = []

for i in range(len(s)-1):
    s = bubble(s)
    s = pops(s)
# print(s)
for i in range(n-1):
    delete(s)
# print(s)

print(len(s))
lst = []
for i in range(len(s)):
    boobs = int(s[i][-1])
    lst.append(boobs)

print(' '.join(map(str, lst)))
