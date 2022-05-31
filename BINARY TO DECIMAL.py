#program to covert binary into decimal (string + number)
binary=int(input('Enter Binary Number: '))
a=len(str(binary))
decimal=0
while binary!=0:
    for i in range(0,a+1,1):
        digit=binary%10
        binary//=10
        decimal=decimal+(digit*(2**i))
print(decimal)