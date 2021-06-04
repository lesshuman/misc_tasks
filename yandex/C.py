'''
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.
'''


n = int(input()) # or sys.stdin.readline().strip(), same for c
res = []
prev = -1
for i in range(n):
    c = input().strip()
    if c!= prev:
        res.append(c)
    prev = c

for elem in res:
	print(elem)
#print(*res,sep='\n') # less memory efficient, according to ya grader
