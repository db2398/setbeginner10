jj,oo=map(int,input().split())
qq=list(map(int,input().split()[:oo]))
zz=[]
for i in qq:
   if(i<=i+1):
     zz.append(i)
print(zz[oo-1])     
