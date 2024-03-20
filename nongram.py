f = []
i_size = j_size = int(input())
def bubble(f):
    flag = True
    while flag:
        flag = False
        for i in range(len(f)-1):
            if f[i+1] < f[i]:
                f[i+1], f[i] = f[i], f[i+1]
                flag = True
    return f


# for rows
for i in range(i_size):
    i__side = list(map(int, input().split('')))
    # j__side = list(map(int, input().split(' ')))
    f.append(i__side)
    a = (int(i_size) - sum(f[i]) - (len(f[i])-1))
    f[i].append(a)
    bubble(f[i])
    if a < f[i][-1]:
        print('YES')
    else:
        print('NO')


# for columns NOT EDITED!!!!!!!!! EDITING IN PROCESS
for i in range(j_s):

    f.append(n_s)
    a = (int(i_s) - sum(f[i]) - (len(f[i])-1))
    f[i].append(a)
    bubble(f[i])
    if a < f[i][-1]:
        print('YES')
    else:
        print('NO')
