V = int(input("enter the nodes"))
E = int(input("enter the no. of edges"))
b={}
for i in range(V):
    b[int(input())]=set()
for i in range(E):
    s,d=map(int,input().split())
    b[s].add(d)

for i in b:
    print(i," : ",b[i])

def path(sn,dn,visited):
    
    visited.add(sn)
    print(sn,end=" ")
    if sn==dn:
        return
    for i in b[sn]:
        if i not in visited:
            path(i,dn,visited)
sn=int(input("enter the starting nodes"))
dn=int(input("enter the destination node"))
visited=set()
path(sn,dn,visited)
