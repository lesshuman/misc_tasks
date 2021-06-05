'''
Даны числа a, b, c, d, e, f. 
Решите систему линейных уравнений 
'''
a,b,c,d,e,f = [float(input()) for _ in "abcdef"]
det = a*d - b*c
detx = e*d - b*f
dety = a*f - e*c
if det!=0:
    x = detx/det
    y = dety/det
    print(2,x,y)
else:
    if (detx == 0 and dety == 0):
        if a == 0 and c == 0 and b == 0 and d == 0:
            if e!=0 or f!=0:
                print(0)
            else:
                print(5)
        elif a == 0 and c == 0:
            if b!=0:
                y = e/b
            elif d!=0:
                y = f/d
            print(4,y)
        elif b == 0 and d == 0:
            if a!=0:
                x = e/a
            elif c!=0:
                x = f/c
            print(3,x)
        else:
            if b!=0:
                k = -a/b
                bb = e/b
            elif d!=0:
                k = -c/d
                bb = f/d
            print(1,k,bb)
    else:
        print(0)
