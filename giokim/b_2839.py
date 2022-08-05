a= int(input())

if a==5 or a==3:
    print(1)
elif a==6:
    print(2)
elif a<8:
    print(-1)
elif a%5==0:
    print(a//5)
elif a%5==3:
    print((a//5)+1)
elif a%5==2 or a%5==4:
    print((a//5)+2)
else:
    print((a//5)+1)
