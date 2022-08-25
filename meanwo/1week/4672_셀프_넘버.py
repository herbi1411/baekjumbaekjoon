
def d():
    total_list = list(range(1, 10001))
    non_self = []

    for i in range(1, 10001):
        # i_sum = 각 자릿수 합
        i_1 = list(str(i))
        i_sum = sum(map(int, i_1))
        # non_self 리스트에 셀프넘버가 아닌 수 저장
        non_self.append(i_sum+i)
        # 셀프넘버가 아닌 수를 차집합 연산
    return list(set(total_list) - set(non_self))

a = d()
#  *: 리스트를 unpacking (요소만 출력)
print(*sorted(a), sep='\n')
