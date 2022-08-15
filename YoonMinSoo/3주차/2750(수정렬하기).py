N = int(input())
lst = [int(input()) for _ in range(N)]


def swap(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp

def compare(a, b):
    return a > b

def bubbleSort(lst):
    rt = lst[:]
    for i in range(len(rt) - 1):
        for j in range(len(rt) - 1 - i):
            if compare(rt[j], rt[j + 1]):
                swap(rt, j, j + 1)
    return rt

def selectionSort(lst):
    rt = lst[:]
    for i in range(len(rt) - 1):
        minIdx = i
        for j in range(i + 1, len(rt)):
            if compare(rt[minIdx], rt[j]):
                minIdx = j
        swap(rt, i, minIdx)
    return rt

def insertionSort(lst):
    rt = lst[:]
    for i in range(len(rt) - 1):
        for j in range(i + 1, 0, -1):
            if compare(rt[j - 1], rt[j]):
                swap(rt, j - 1, j)
            else:
                break
    return rt

# print(*bubbleSort(lst), sep='\n')
# print(*selectionSort(lst), sep='\n')
print(*insertionSort(lst), sep='\n')