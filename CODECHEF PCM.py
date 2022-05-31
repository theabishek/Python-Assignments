#PCM
for i in range(int(input())):
    p_count,c_count,m_count=0,0,0
    str=[i for i in input()]
    if 'P' in str:
        p_count+=1
        if 'C' in str:
            c_count+=1
            if 'M' in str:
                m_count+=1
    if p_count==c_count==m_count==1:
        print('YES')
    else:
        print('NO')