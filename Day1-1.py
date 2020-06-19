#Day1-1
for i in range(int(input())):
    m,n=input().split()
    m,n=int(m),int(n)
    l={}
    for j in range(2,int(n**0.5)+1):
        for k in range(max(m//j,2),(n//j)+1):
            l[j*k]=1
    for j in range(max(m,2),n+1):
        if j not in l:
            print(j)
    print()
