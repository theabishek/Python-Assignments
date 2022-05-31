#WAP to count number character in text file.
with open('file2.txt','w+') as f:
    while True:
        str=input()
        if str=='exit':
            break
        else:
            f.write(str)
            f.write('\n')
    f.seek(0,0)
    count=0
    for i in (f.read()):
        count+=1
    print('number of character is ',count)
    print(f.read())