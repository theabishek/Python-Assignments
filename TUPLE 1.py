#WAP to enter elements in tuple and store tuples in list.
lst=[]
x=int(input('Enter number of rows: '))
y=int(input('Enter number of column: '))
for i in range(x):
    tupl=()
    for j in range(y):
        y1=int(input('Enter Elements: '))
        tupl+=y1,
    lst.append(tupl)
print(lst)

lst1=[(9, 8), (5, 6)]
lst2=[(5, 6), (8, 4)]
lst3=[]
if len(lst1)==len(lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            a=len(lst1[i])
            b=len(lst2[j])