def ally(n): 
    c=0
    for i in range(1,n+1):
        if i>0 and i<10:
            c+=1
        else:
            s=str(i)
            k=True
            for j in range(0,len(s)-1):
                if s[j]>s[j+1]:
                    k=False
                    break
            if k:
                c+=1
    return c
#{ 
#  Driver Code Starts



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ally(n))
