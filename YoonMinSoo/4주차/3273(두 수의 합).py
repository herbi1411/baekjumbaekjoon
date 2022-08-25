N = int(input())
lst = list(map(int, input().split()))
fNum = int(input())
cnt = 0
s = 0
e = len(lst) - 1
lst.sort()

while s < e:
    if lst[s] + lst[e] == fNum:
        cnt += 1
        e -= 1
    elif lst[s] + lst[e] > fNum:
        e -= 1
    else:
        s += 1
print(cnt)