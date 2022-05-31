#WAP to print fibonacci series in dictionary

d={}
fab=0
b=1
n=int(input('Enter Number Of Elements: '))
for i in range(1,n+1):
    k=i
    v=fab
    a=b
    b=fab
    fab=a+b
    d.update({k:v})
print(d)
