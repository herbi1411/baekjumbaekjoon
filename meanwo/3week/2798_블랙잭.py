n, m = map(int, input().split())
A = list(map(int, input().split()))


sum_case = 0
max_case = 0

# 뽑은 숫자들을 넣을 리스트
sum_list = [0]*3

# 숫자별 갯수(1번 뽑으면 1씩 차감)
masking_list = [1]*n

for i in range(n):
    # 세 숫자를 다 뽑고 나면 숫자별 갯수 리스트를 1로 초기화
    masking_list = [1] * n

    sum_list[0] = A[i]*masking_list[i]
    masking_list[i] -= 1
    for j in range(n):
        if masking_list[j] == 1:
            sum_list[1] = A[j] * masking_list[j]
            masking_list[j] -= 1
            for k in range(n):
                if masking_list[k] == 1:
                    sum_list[2] = A[k]*masking_list[k]

                    # 뽑은 세 숫자의 합
                    sum_case = sum(sum_list)

                    # 합이 M이 넘지 않는 최대값 조회
                    if (sum_case > max_case) and (sum_case <= m):
                        max_case = sum_case

print(max_case)