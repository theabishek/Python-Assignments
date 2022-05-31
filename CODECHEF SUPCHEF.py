#SUPCHEF
for i in range(int(input())):
    m,n,k=map(int,input().split())
    if n*k<m:
        print('YES')
    else:
        print('NO')