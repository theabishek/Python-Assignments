#PYTHON PROGRAM TO SHORT NAME
def shortname():
    name=input('Enter Full Name: ')
    l=len(name)
    count=0
    space=' '
    initial=name[0]+space 
    shortname='' #empty list to store short name.
    for i in range(l):
        if name[i]==' ':
            count+=1
            lastname=name[i+1:]
    for i in range(0,l):
        if count>1:
            if name[i]==' ':
                shortname=shortname+name[i+1]+space
                count-=1
        else:
            break
    print(initial+shortname+lastname)

shortname()