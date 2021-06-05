'''
Последовательность чисел назовем симметричной, если она одинаково читается как слева направо, так и справа налево. 
Например, следующие последовательности являются симметричными: 1 2 3 4 5 4 3 2 1  1 2 1 2 2 1 2 1.
Вашей программе будет дана последовательность чисел. Требуется определить, какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной. 

Test cases:
[in]: 9
      1 2 3 4 5 4 3 2 1
[out]: 0

[in]: 5
      1 2 1 2 2
[out]: 3
       1 2 1
       
[in]: 5
      1 2 3 4 5
[out]: 4
       4 3 2 1
'''
n = int(input())
s = list(map(int,input().split()))

def is_symmetric(s):
    def helper(s):
        return s == s[::-1]
    res = []
    if helper(s):
        return (0,)
    for i in range(n):
        res.insert(-i,s[i])
        if helper(s + res):
            return (i+1, ' '.join(map(str,res)))
            
print(*is_symmetric(s),sep='\n')