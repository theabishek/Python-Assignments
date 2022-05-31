#PAIRPR1
for i in range(int(input())):
    n=int(input())
    l=[]
    for i in range(1,n+1):
        count_0=0
        for j in range(1,i+1):
            if i%j==0:
                count_0+=1
        if count_0==2:
            l.append(i)
    l2=[]
    count=len(l)*len(l)
    for i in l:
        for j in l:
            if i+j==n:
                l2.extend([i,j])
                break
            else:
                count-=1
    if count==0:
        print('-1 -1')
    else:
        print(l2[0],l2[1])