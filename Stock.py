"""
For a stock, we have a series of N daily price quotes. For each day, the task is to find how many such, continous days (including current day) 
are there prior to the current day where the price of the stock was less than or equal to the price on the current day.
6 -- value of n, denoting number of days
100 -- 1st day stock price
60 -- 2nd day stock price
70 -- 3rd day stock price
65 -- 4th day stock price
80 -- 5th day stock price
85 -- 6th day stock price
output: 1 2 1 4 5
"""

#using recursion
def rec(l,s,e):
    if s==e or l[s]>=l[e]:
        return 1+rec(l,s,e-1)
    if e==-1 or l[s]<l[e]:
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



