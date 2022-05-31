#WAP TO SEPERATE EVEN AND ODD NUMBERS IN LIST.
l=[]
num=int(input('Enter Number of Elements :'))
for i in range(0,num):
    l.append(int(input('Enter Element :')))
print(l)
even=[]
odd=[]
x=len(l)
for i in range(x):
    if (l[i]%2==0):
        even.append(l[i])
    elif(l[i]%2==1):
        odd.append(l[i])
        k=sum(even)
print('this is even list',even, 'and the sum of even list is ',sum(even))
print('this is odd list',odd,'sum of the list is ',sum(odd))
