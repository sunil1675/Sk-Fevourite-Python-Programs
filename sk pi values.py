f=open('pivalue.txt','w',encoding='utf-16 LE')
n=22
for i in range(200):
    q=n//7
    r=n % 7
    print(q,end=" ")
    t=str(q)
    f.write(t)
    f.write(str(" "))
    
    if r<7:
        n=int(str(r) + '0')
    else:
        n=r
f.close()
