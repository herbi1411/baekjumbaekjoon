#테스트 케이스의 횟수
C = int(input())
for i in range(C):
    #입력
    a = list(map(int, input().split()))
    score = a[1:]
    # 테스트케이스 별 평균
    aver = sum(score)/(len(score))

    # 평균을 넘는 학생 판별
    count = 0
    for j in range(len(score)):
        if score[j] > aver:
            count += 1
    #백분율 소수점 셋째자리까지 출력
    print('%.3f%%' % (100 * count/len(score)))

