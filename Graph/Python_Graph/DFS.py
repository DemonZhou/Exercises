# -*- coding: utf-8 -*-
def DFS_Visit(graph, u, vlist):
    if u in vlist:
        return
    vlist.append(u)
    for v in graph[u]:
        DFS_Visit(graph, v, vlist)

def DFS_Sort(graph, u, vlist, L):
    if u in vlist:
        return 
    vlist.append(u)
    for v in graph[u]:
        DFS_Sort(graph, v, vlist, L)
    L.insert(0,u) #insert it onto the front of a linked list


def DFS(graph):
    vlist = []
    for v in graph.keys():
        DFS_Visit(graph, v, vlist)
        print vlist


def TopoLogical_Sort(graph):
    vlist = []
    topolist = []
    for v in graph.keys():
        DFS_Sort(graph, v, vlist, topolist)
    return topolist

# testcase
graph = {
    1: [2, 3],
    2: [],
    3: [4, 5],
    4: [6],
    5: [],
    6: []
}

#DFS(graph)
print TopoLogical_Sort(graph)
