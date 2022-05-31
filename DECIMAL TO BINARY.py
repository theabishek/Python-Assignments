#Program to convet decimal into binary.
num=int(input('Enter Number: '))
binary=0
count=0
while num!=0:
    binary=num%2*(10**count)+binary
    num//=2
    count+=1
print(binary)