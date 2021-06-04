"""
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному
массиву только один раз.
"""

n = int(input())
max_res = 0
prev = -1
res = -1
for i in range(n):
    c = int(input())
    if c == 1 and prev != 1:
        res = 1
        prev = 1
    elif c == 1 == prev:
        res+=1
    if (c == 0 and prev == 1) or (i == n-1):
        if res > max_res:
            max_res = res
        res = -1
        prev = -1
    else:
        continue  
print(max_res)

"""
Альтернативное решение:
n = int(input())
max_res = 0
res = 0
for i in range(n):
    c = int(input())
    if c == 1:
        res+=1
    else:
        if res > max_res:
            max_res = res
        res = 0
print(max_res if max_res > res else res)
"""
