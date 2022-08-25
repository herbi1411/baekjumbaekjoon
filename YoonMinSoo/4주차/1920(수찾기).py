N = int(input())
arr = list(map(int, input().split()))
aset = set()
for v in arr:
    aset.add(v)
M = int(input())
arr2 = list(map(int, input().split()))
for v2 in arr2:
    if v2 in aset:
        print(1)
    else:
        print(0)