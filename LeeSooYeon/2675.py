t = int(input())

for test_case in range(1, t+1) :
    s = input().split()
    text = str(s[1])
    num = int(s[0])
    new_text = []

    for i in text :
        new_text.append(i * num)

    p = ''.join(new_text)
    print(p)