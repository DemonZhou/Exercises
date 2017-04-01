# -*- coding: utf-8 -*-
def DFS_Visit(graph, u, vlist):
    vlist.add(u)
    for v in graph[u]:
        if not v in vlist:
            DFS_Visit(graph, v, vlist)


def DFS_Sort(graph, u, vlist, L):
    vlist.add(u)
    for v in graph[u]:
        if not v in vlist:
            DFS_Sort(graph, v, vlist, L)
    if u not in L:
        L.append(u)


def DFS(graph):
    vlist = set()
    for v in graph.keys():
        DFS_Visit(graph, v, vlist)
        print vlist


def TopoLogical_Sort(graph):
    vlist = set()
    topolist = []
    for v in graph.keys():
        DFS_Sort(graph, v, vlist, topolist)
    return topolist


graph = {
    1: [2, 3],
    2: [],
    3: [4, 5],
    4: [6],
    5: [],
    6: []
}

# DFS(graph)
print TopoLogical_Sort(graph)
