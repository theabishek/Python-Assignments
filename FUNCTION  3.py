#WAP to reduce same elements from a list and print UNIQUE LIST using function.
def unique(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    print(l2)

l=[]
n=int(input('Enter number of elements in the list: '))
for i in range(n):
    l.append(int(input('Enter Element: ')))
unique(l)