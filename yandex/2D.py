'''
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество таких элементов. 

Test cases:
[in]: 1 2 3 4 5
[out]: 0

[in]: 5 4 3 2 1
[out]: 0

[in]: 1 5 1 5 1
[out]: 2
'''
seq = list(map(int,input().split()))
res = 0
for i in range(1,len(seq)-1):
	if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
		res+=1
print(res)
