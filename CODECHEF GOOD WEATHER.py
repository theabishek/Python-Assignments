#CODECHEF GOOD WEATHER
for i in range(int(input())):
    ones=zeroes=0
    x=[int(num)for num in input().split(' ',6)]
    for i in x:
        if i==0:
            zeroes+=1
        elif i==1:
            ones+=1
    if ones>zeroes:
        print('YES')
    else:
        print('NO')