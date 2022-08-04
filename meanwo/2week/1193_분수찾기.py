a = int(input())

# a가 주어졌을 때 대각선으로 몇 번째 배열인지 찾기
# 등차수열 합 공식과 완전제곱식 이용
x = (2*a+0.25)**0.5 - 0.5

# 내장함수 없이 올림 구현
n = int(-(-x//1))

# 이전 배열들의 갯수
pre_n = sum(list(range(1, n)))

# n번째 배열의 몇번 째 수인지 구하기
n_order = a - pre_n

# 홀수 번째 배열 일때(우상단 방향 진행)
if n % 2 == 1:
    print(f'%d/%d' % (n+1-n_order, n_order))
# 짝수 번째 배열 일때(좌하단 방향 진행)
else:
    print(f'%d/%d' % (n_order, n+1-n_order))