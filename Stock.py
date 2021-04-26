#using recursion
def rec(l,s,e):
    if s==e or l[s]>l[e]:
        return 1+rec(l,s,e-1)
    if e==-1 or l[s]<=l[e]:
        return 0

    
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(1,end=" ")
for i in range(1,n):
    #using loops
    '''c=1
    for j in range(i-1,-1,-1):
        if l[i]>l[j]:
            c+=1
        else:
            break'''
    print(rec(l,i,i),end=" ")



