from collections import deque
T = int((input)())
for i in range(T):
    n = int(input())
    d = deque(map(int,input().split()))
    hd = abs(len(d)//2 - d.index(min(d)))
    for j in range(n):
        if len(d)<3:
            print('Yes')
            break
        elif max(d[0],d[-1]) < max(list(d)[1:-1]):
            print('No')
            break 
        elif min(d) == max(d):
            print('Yes')
            break
        elif len(d)>3:
            print('Yes')
            break
        elif sorted(list(d)[:len(d)//2+hd]) == list(reversed(list(d)[:len(d)//2+hd])) \
                and sorted(list(d)[len(d)//2+hd:]) == list(d)[len(d)//2+hd:]:
            print('Yes')
            break
        elif sorted(d) == list(d) or list(reversed(d)) == list(d):
            print('Yes')
            break
        else:
            print('No')
            break
