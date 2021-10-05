
V = int( input("enter the no. of nodes") )
E = int( input("enter the no. of edges") )
table={}
print("enter the vertices ->")
for i in range(V):
    table[int(input())]=set()
for i in range(E):
    s,d,w=map(int,input().split())
    table[s].add(tuple((d,w)))
    table[d].add(tuple((s,-1*w)))

for i in table:
    print(i," -> ",table[i])



def dfsr(sn,visited):
    visited.add(sn)
    print(sn,end=" ")

    for i in table[sn]:
        if i[0] not in visited:
            dfsr(i[0],visited)

visited=set()
sn = int( input("enter the node taken as source node"))
dfsr(sn,visited)