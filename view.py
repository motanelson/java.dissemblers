import os
import copy
print("\033c\033[47;31m/give me the class file to view ? ")
a=input().strip()
#a="Hello.class"
f1=open(a,"rb")
b=f1.read()
f1.close()
j=False
t=False
l=[]
pp=0
ui=bytearray()
p=False
o=False
count=0
for c in b:
    if t and p:
        if c>31 and c<129:
            o=True
        else:
            o=False
        p=False    
    if t and o:
        if c>31 and c<129:
            cc=chr(c)
    
            print(cc,end="")
            j=True
    if t and oo and o==False:
        ui=ui+bytes([c])   
    if len(l)==2:
        l.append(c)
        i:int=int(c)
        pp=c
        print("\n"+str(count)+"   "+str(i)+" " ,end =" ")
        p=True
        t=True
        oo=True
        count=count+1
    if c==1:
        l.clear()
        l.append(1)
        oo=False
        if t and pp>0:
            f1=open("/tmp/out.bin","wb")
            f1.write(ui)
            f1.close()
            os.system("rasm2 -a java -D -B -f /tmp/out.bin")
        ui=bytearray()
    if c==0 and len(l)==1:
        if l[0]==1:
            l.append(0)
   