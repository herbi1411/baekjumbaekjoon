N = int(input())

# 두 봉지 갯수의 합을 total에 저장
total = 0
# 5kg 봉지를 많이 쓰는 경우의 수부터 계산
for i in range((N//5), -1, -1):
    total += i
    N_temp = N - 5*i
    if N_temp % 3 == 0:
        total += N_temp//3
        #최소 봉지 갯수를 구하면 반복문 종료
        print(total)
        break
    # 반복문을 다 조회하는 동안 맞아 떨어지지 않으면 -1 출력
    elif i == 0:
        print(-1)
        break
    # 반복문을 돌며 맞아 떨어지지 않으면 봉지 갯수 초기화
    else:
        total = 0