'''
Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.

Test cases:
[in]: 1 7 9
[out]: YES

[in]: 1 9 7
[out]: NO

[in]: 2 2 2
[out]: NO
'''

def is_increasing(s):
	if len(s) == 0:
		return "NO"
	for i in range(1,len(s)):
		if s[i] <= s[i-1]:
			return "NO"
	return "YES"

s = list(map(int,input().split()))	
print(is_increasing(s))
