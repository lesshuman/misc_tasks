'''
Наибольшее произведение двух чисел.
Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально. Выведите эти числа в порядке неубывания.
Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен. 
Test cases:
[in]: 4 3 5 2 5
[out]: 5 5 

[in]: -4 3 -5 2 5
[out]: -5 -4
'''
seq = list(map(int,input().split()))
def max2product(s,l):
    max1 = seq[0]
    max2 = seq[1]
    min1 = 0
    min2 = 0
    if len(seq) == 2:
        return ' '.join(sorted(map(str,seq)))
    for i in range(l):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
        if seq[i] < 0 and seq[i] < min1:
            min2 = min1
            min1 = seq[i]
        elif seq[i] < 0 and seq[i] < min2:
            min2 = seq[i]
		
    if max1*max2 > min1*min2:
	    return f'{max2} {max1}'
    else:
	    return f'{min1} {min2}'
	    
print(max2product(seq,len(seq)))

'''
Наибольшее произведение трех чисел.
В данном списке целых чисел найдите три числа,произведение которых максимально. Выведите три искомых числа в любом порядке. 
Test cases:
[in]: 3 5 1 7 9 0 9 -3 10
[out]: 10 9 9 

[in]: -5 -30000 -12
[out]: -5 -30000 -12
'''
seq = list(map(int,input().split()))
s = sorted(seq)
def max3prod(s,l):
	if l == 3:
		return ' '.join(map(str,s))
	if s[0]*s[1]*s[-1] > s[-1]*s[-2]*s[-3]:
	    return ' '.join(map(str,s[0:2])) + ' ' + str(s[-1])
	else:
	    return ' '.join(map(str,s[l-3:l]))

print(max3prod(s,len(s)))
