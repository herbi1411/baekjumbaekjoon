n = int(input())

# 한수를 담을 리스트
numbers = []

# 1보다 크거나 같고, n보다 작거나 같은 수 i
for i in range(1, n+1) :
    i = str(i)

# 세 자리 숫자의 경우, 100의 자리수와 10의 자리수의 차가 10의 자리수와 1의 자리수의 차와 같을 경우
# 한수 리스트에 담음
# 순서가 바뀌어도 상관 없도록 조건 추가
if int(i) >= 100 :
	if(int(i[1]) - int(i[0])) == (int(i[2]) - int(i[1])) :
            numbers.append(i)
	elif(int(i[0]) - int(i[1])) == (int(i[1]) - int(i[2])) :
            numbers.append(i)

# 두 자리 숫자의 경우, 앞 뒤가 차가 있는 경우와 같은 경우 모두 한수 리스트에 담음 
elif int(i) >= 10 :
	if int(i[1])  > int(i[0]) :
            numbers.append(i)
	elif int(i[0]) > int(i[1]):
            numbers.append(i)
	elif int(i[0]) == int(i[1]):
            numbers.append(i)

# 한 자리 숫자의 경우, 이해는 안 가는데 문제 입출력에서 1의 한수 개수는 1이라고 해서
# 한 자리 수는 모두 한수가 되는 것 같음. 모두 한수 리스트에 담음
elif int(i) < 10 :
        numbers.append(i)

# 한수 리스트에 담긴 숫자의 개수 출력
print(len(numbers))