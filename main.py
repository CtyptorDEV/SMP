def factorisation(n):
    l = [1]
    i = 2
    while i*i <= n:
        while n % i == 0:
            l.append(i)
            n = n / i
        i = i + 1
    if n != 1:
        l.append(int(n))
    return l

print(list(range(3, 1, -1)))
