def f(n):
    if n > 1:
        return f(n-1) + f(n-2)
    elif n == 0:
        return 0
    elif n == 1:
        return 1


k = int(input())
a = f(k)

print(a)
