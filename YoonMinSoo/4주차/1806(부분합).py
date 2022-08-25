INF = 2147483647
N, S = map(int, input().split())
arr = list(map(int, input().split()))

minLen = INF
s = 0
e = 0
temp = 0

while s < len(arr):
    if temp < S:
        if e >= len(arr):
            break
        temp += arr[e]
        e += 1

    else:
        minLen = min(minLen, e - s)
        temp -= arr[s]
        s += 1

if minLen == INF:
    print(0)
else:
    print(minLen)