n = int(input())
answer = 0

for i in range(1,n+1): # 1부터 n까지 다해보기
    nstr = str(i)
    strlen = len(nstr)
    flag = True
    interval = 0

    if strlen <= 2: # 길이가 2보다 작다면 그 수는 한수
        answer+=1
        continue

    else:
        interval = ord(nstr[1]) - ord(nstr[0])
        for j in range(len(nstr)-1):
            if interval == ord(nstr[j+1]) - ord(nstr[j]):
                continue
            else:
                flag = False
                break

        if flag is True: # 수의 모든 자릿수에서 인접한 자리의 차이가 같다면
            answer += 1

print(answer)