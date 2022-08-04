def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))

#  시간복잡도 O(2^N) 