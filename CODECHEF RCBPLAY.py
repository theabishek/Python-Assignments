#RCBPLAY
for i in range(int(input())):
    x,y,z=map(int,input().split())
    if (z*2)+x>=y:
        print('YES')
    else:
        print('NO')