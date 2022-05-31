#CODECHEF sandmax
lst=[]
n=int(input())
for i in range(n):
    l,m,n=map(int,input().split())
    if (l>m and l<n)or(l>n and l<m):
        s=l
    elif (m>l and m<n)or(l>m and n<m):
        s=m
    else:
        s=n
    lst.append(s)
for i in lst:
    print(i)
