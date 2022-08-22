T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    Max = 0

    def catch(y,x):
        sum = 0
        for i in range(M):
            for j in range(M):
                sum += arr[i+y][j+x]
                if i+y > N or j+x > N: continue
        return sum

    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ret = catch(i,j)
            if ret > Max:
                Max = ret


    print(f'#{tc} {Max}')