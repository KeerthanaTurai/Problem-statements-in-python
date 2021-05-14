n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for i in range(n-1):
    print(sum(l[i+1:]),end=" ")
print(0)
