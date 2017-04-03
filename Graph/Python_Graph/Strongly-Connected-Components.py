
# -*- coding: utf-8 -*-  
def transpose(graph):
    graphT = {}
    for key in graph.keys():
        graphT[key] = []
    for key,value in graph.items():
        for v in value:
            graphT[v].append(key)
    return graphT

def DFS_Visit(graph,u,vlist,vlist2):
    if u in vlist:
        return 
    vlist.append(u)
    for v in graph[u]:
        DFS_Visit(graph,v,vlist,vlist2)
    vlist2.append(u)# to calculate u.f 即每个点的离开时间顺序

def DFS_Visit_2(graph,u,vset):
    if u in vset:
        return
    vset.add(u)
    for v in graph[u]:
        DFS_Visit_2(graph,v,vset)

def DFS(graph):
    vlist = []
    vlist2 = []
    for u in graph.keys():
        DFS_Visit(graph,u,vlist,vlist2)
    return vlist2

def DFS_2(graph,numlist):
    vset = set()
    for u in numlist:
        oldvset = vset.copy()
        DFS_Visit_2(graph,u,vset)
        if vset - oldvset != set():
            yield vset - oldvset

def Strongly_Connected_Components(graph):
    graphT = transpose(graph)
    numlist = DFS(graph)
    numlist.reverse()
    print 'Strongly-Connected-Components are:'
    for i in DFS_2(graphT,numlist):
        print i
    


graph = {
   'a':['b'],
   'b':['e','c','f'],
   'c':['d','g'], 
   'd':['c','h'],
   'e':['a','f'],
   'f':['g'],
   'g':['f','h'],
   'h':['h'],
}
Strongly_Connected_Components(graph)