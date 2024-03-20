def non_factorisation(n):
    l = [1]
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            l.append(i)
            l.append(int(n/i))
    return l

a, b = map(int, input().split(' '))

min_n = b
for i in range(b, a-1, -1):
    if a == 1:
        min_n = 1
        break
    n = sum(non_factorisation(i))
    if n == 1:
        min_n = i
        break
    elif i == b:
        min = n/i
    elif n/i < min:
        min = n/i
        min_n = i

print(min_n)
