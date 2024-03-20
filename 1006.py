# не закончено

n = int(input())
l = []
for i in range(10**(n - 1), 10**n):
    m = [int(i) for i in str(i)]
    a = int(n/2)
    print(m)
    if sum(m[0:a]) == sum(m[a:-1]):
        l.append(1)
    print(sum(m[0:a]), sum(m[a:-2]))
print(len(l))

print(l)
