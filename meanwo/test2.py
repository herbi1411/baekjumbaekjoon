a = int(input())

sum_a = a//10 + a%10
new_a = (a%10)*10 + sum_a
count = 1
while True:
    if new_a == a:
        break
    else:
        sum_a = new_a//10 + new_a % 10
        new_a = (new_a%10)*10 + sum_a % 10
    count += 1
print(count)

