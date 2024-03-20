import time

def non_factorisation(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(int(i))
    return l
def bubble(lst):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst)-1):
            if lst[i+1] < lst[i]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
                flag = True
    return lst


a, b = map(int, input().split(' '))

start = time.time()
m = []
for n in range(b, a-1, -1):
    m.append(non_factorisation(n))
summa = []
# c = ()
for i in range(len(m)):
    c = sum(m[i])
    summa.append(c)
    c = ()
triv = []
# t = ()
a_1 = a
for i in range(len(summa)):
    t = summa[i] / a_1
    triv.append(t)
    a_1 = a_1 + 1
    t = ()
triv_1 = triv.copy()
bubble(triv)
# print(m)
# print(summa)
# # print(c)
# # print(t)
# print(triv)
# print(triv_1)
# print(a)
for i in range(1, len(triv)):
    if triv[0] != triv_1[i]:
        continue
    else:
        print(a+i)

end = time.time()

print(end - start)
