num = int(input())
arr = list(map(int,input().split()))
arr.sort()

rst = 0
for i in range(num):
    rst+=(num-i)*arr[i]
print(rst)