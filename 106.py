bhavya,u=map(int,input().split())
list=input().split()
d1=[]
for i in list:
   if(int(i)%2!=0):
    d1.append(i)
print(d1[u-1])
