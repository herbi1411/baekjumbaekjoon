# total_list : 범위, check_list : 에라토스테네스의 체
total_list = list(1 for i in range(0, 10001))
check_list = list(range(2, int(10000**0.5)+1))
n_prime_factor = []

#소인수의 배수에 해당하는 인덱스에 0 할당
for check_number in check_list:
    for i in range(check_number*2, 10001, check_number):
        total_list[i] = 0

# 범위 내의 소인수를 n_prime_factor에 저장
for j in range(len(total_list)):
    if j >= 2 and total_list[j] == 1:
        n_prime_factor.append(j)

#T는 테스트 케이스
T = int(input())

for i in range(T):
    n = int(input())
    k = 0

# n의 절반으로부터 1씩 멀어지는 두 수가 소인수 리스트에 존재하면 반복문 종료하고 반환
    while True:
        if (n/2 + k) in n_prime_factor and (n/2 -k) in n_prime_factor:
            p_n1 = int(n/2-k)
            p_n2 = int(n/2+k)
            print(p_n1, p_n2)
            break
        else:
            k += 1

