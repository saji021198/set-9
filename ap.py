a,d,n=map(int,input().split())
f=[]
sum = 0
for i in range (0,n):
    k = a + (i*d)
    f.append(k)
for i in f:
    sum=sum+i
print(sum)

