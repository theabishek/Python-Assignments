#WAP to find the sum of a list using function.
def listsum(l):
    print(sum(l),' is the sum of the list.')

l=[]
n=int(input('Enter number of elements in the list: '))
for i in range(n):
    l.append(int(input('Enter Element: ')))
listsum(l)
