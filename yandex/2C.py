'''
Найти в массиве элемент, самый близкий по величине к  данному числу. 

Test cases:
[in]: 5
      1 2 3 4 5
      6
[out]: 5

[in]: 5
      5 4 3 2 1
      3
[out]: 3
'''

l = int(input())
seq = list(map(int,input().split()))
x = int(input())
difs = [(s,abs(x - s)) for s in seq]
difs.sort(key=lambda p:p[1])
print(difs[0][0])
