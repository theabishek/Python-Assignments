#WAP to find factorial of a number using function
def facto(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

x=int(input('Enter a number: '))
facto(x)