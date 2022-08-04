def numerator(gap,index):
    if index >= int(gap/2) + 1:
        return index - int(gap/2)
    else:
        return int(gap/2) - index + 1
def denominator(gap,index):
    if index > int(gap/2) + 1:
        return (int(gap/2) + 1)*2 - index
    else:
        return index

target = int(input())
if target ==1:
    print("1/1")
else:
    gap = 3
    start = 1
    while start + gap <= target:
      start += gap
      gap += 4

    r1 = numerator(gap,target-start+1)
    r2 = denominator(gap,target-start+1)

    print("%d/%d"%(r1,r2))