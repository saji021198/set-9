m=list(input())
n=[]
for i in m:
    if i not in n:
        n.append(i)
if(m==n):
    print("Yes")
else:
    print("No")

