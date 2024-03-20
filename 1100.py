# не прошел по памяти!!!

n = int(input())

k = []
for i in range(n):
    k.append(list(map(int, input().split(' '))))
flag = True
while flag:
    flag = False
    for i in range(len(k)-1):
        if k[i][1] < k[i+1][1]:
            k[i], k[i+1] = k[i+1], k[i]
            flag = True
for i in range(len(k)):
    print(k[i][0], k[i][1])
