#PROGRAM TO SUM OF VALUES OF DICTONARY.

d={}
valuesum=0
n=int(input('Enter number of elements: '))
for i in range(n):
    k=int(input('Enter Key: '))
    v=int(input('Enter Values: '))
    d.update({k:v})
print(d)
for i in d.values():
    valuesum+=i
print('sum of values is ',valuesum)
print('List of Values in asscending order is ',(sorted(d.values())))