#WAP to count number of words in text file.
with open('file2.txt','w+') as f:
    while True:
        str=input()
        if str=='exit':
            break
        else:
            f.write(str)
            f.write('\n')
    f.seek(0,0)
    str=f.read()
    print('no of words is ',len(str.split()))