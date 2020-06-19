# your code goes here
l=[]
p=int(input())
for i in range(p):
    l1=list(map(str,input().split()))
    l.append(l1)
for i in range(p):
    m=l[i][0]
    n=l[i][1]
    m=int(m[-1::-1])
    n=int(n[-1::-1])
    r=str(m+n)
    r=int(r[-1::-1])
    print(r)