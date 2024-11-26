def getrecord(opt):
    a=[]
    print("*"*41)
    print("FILL INFORMATION OF A RECORD".center(41))
    print("="*41)
    for i in range(len(opt)):
        t=input(f"ENTER VALUE FOR {opt[i].upper()} :".ljust(40," "))
        a.append(t)
    print("="*41)
    input("\n\nPress any key to continue........")
    return a

def drawmenu(title,opt):
    print("*"*41)
    print(title.title().center(41))
    print("*"*41)
    for i in range(len(opt)):
        print("|\t\t",i+1,".",opt[i].upper(),"\t\t|")
    
    print("|\t\t",0,".","QUIT","\t\t|")
    print("*"*40)
    ch=int(input('ENTER YOUR CHOICE '))
    return ch


#ch=drawmenu('stack operation',['push','pop','print'])
drawmenu(title,opt)
rec=getrecord(["roll number",'name','total','percentage','Date of birth','grade'])


