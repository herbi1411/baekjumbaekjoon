a, b = map(int, input().split())
total_list = list(1 for i in range(0, b+1))

#에라토스테네스의 체
check_list = list(range(2, int(b**0.5)+1))

#소인수의 배수에 해당하는 인덱스에 0 할당
for check_number in check_list:
    for i in range(check_number*2, b+1, check_number):
        total_list[i] = 0

#범위 내의 소인수 출력
for j in range(len(total_list)):
    if j != 1 and j >= a and total_list[j] == 1:
        print(j)
