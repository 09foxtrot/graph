from collections import deque
V = int(input("enter the no. of nodes"))
E = int(input("enter the no. of edges"))
table={}
print("enter the vertices.")
for i in range(V):
    table[int(input())]=set()
for i in range(E):
    s,d,w=map(int,input().split())
    table[s].add(tuple((d,w)))
for i in table:
    print(i," -> ",table[i])
sn=int(input("enter the node taken as source node  "))
visited={}
for i in table:
    visited[i]=0
q=deque([])
bfs=[]
visited[sn]=1
q.append(sn)
print(q)
while(len(q)!=0):
    a=q.popleft()
    for i in table[a]:
        b=i[0]
        if visited[b]!=1:
            visited[b]=1
            q.append(b)
    print(q)     
    bfs.append(a)
    print(bfs)

print(bfs)

