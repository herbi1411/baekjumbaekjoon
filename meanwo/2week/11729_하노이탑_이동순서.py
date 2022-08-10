n = int(input())

start = 1
temp = 2
end = 3



def hanoi_tower(n, start, temp, end):
    if n == 1:
        print("{} {}".format(start, end))
    else:
        hanoi_tower(n - 1, start, end, temp)
        print("{} {}".format(start, end))
        hanoi_tower(n - 1, temp, start, end)


print(2**n-1)
result = hanoi_tower(n, 1, 2, 3)
result