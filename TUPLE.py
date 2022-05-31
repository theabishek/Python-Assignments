#Program to write a program to enter values from user and store it in tuple.
tpl=()
x=int(input('Enter Number of Elements: '))
for i in range(x):
    y=int(input('Enter Elements: '))
    tpl+=y,
print(tpl)
type(tpl)

