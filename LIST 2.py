#WAP TO PRINT SUM OF NEGATIVE AND SUM OF POSITIVE ELEMENTS FROM LIST.
def sum():
    l=[]
    negsum=0
    possum=0
    n=int(input('Enter Number of elements in list: '))
    for i in range(n):
        l.append(int(input('Enter an Integer: ')))
    for i in l:
        if i<0:
            negsum+=i
        else:
            possum+=i
    print('sum of negative integer in list is ',negsum)
    print('sum of positive integer in list is ',possum)
sum()