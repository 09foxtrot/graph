V = int( input("enter no. of nodes ") )
E = int( input("enter no. of edges ") )
table = {}
for i in range(V):
    table[ int( input() ) ]= set()
for i in range(E):
    s,e,w = map( int , input().split() )
    table[s].add( tuple( ( e,w ) ))
    #table[e].add( tuple( (s,-1*w) ) )
for i in table:
    print(i,"  ->   ",table[i])
 