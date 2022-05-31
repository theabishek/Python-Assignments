f=open('avin.txt','r')
f.seek(0,0)
sum=0
str=f.read()
print(str)
for i in str:
    if i=='\n':
        sum+=1
print(sum)
f.close()