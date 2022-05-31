#CODECHEF greedy puppy
n=int(input())
for i in range(n):
    l=[]
    n,k=map(int,input().split())
    for i in range(1,k+1):
        l.append(n%i)
    print(max(l))
