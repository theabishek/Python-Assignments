#PROGRAM TO PRINT FREQUENCY OF CHARACTER IN STRING.

x=input('Enter String: ')
dict={}
for i in x:
    count=0
    for j in x:
        if i==j:
            count+=1
            k=count
            dict.update({i:k})
        else:
            continue
print(dict)