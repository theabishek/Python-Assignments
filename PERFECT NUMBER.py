a=int(input('Enter a number to check PERFECT :'))
sum=0
copy=a
n=1
while(n<a):
    if(a%n==0):
        sum=sum+n
    n=n+1
if(sum==copy):
    print('Yes it is PERFECT number')
else:
    print('No it is not PERFECT number')