#CODECHEF mahasena
even=0
odd=0
n=int(input())
numbers =[int(num) for num in input().split(" ", n-1)]
for i in numbers:
    if (i%2)==0:
        even+=1
    else:
        odd+=1
print(even,odd)
if odd>=even:
    print('NOT READY')
else:
    print('READY FOR BATTLE')
