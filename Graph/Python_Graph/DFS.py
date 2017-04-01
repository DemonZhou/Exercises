# -*- coding: utf-8 -*-
def DFS_Visit(graph, u, vlist):
    vlist.add(u)
    for v in graph[u]:
        if not v in vlist:
            DFS_Visit(graph, v, vlist)


def DFS(graph):
    vlist = set()
    for v in graph.keys():
        DFS_Visit(graph, v, vlist)
        print vlist


graph = {
    1: [2, 3],
    2: [3],
    3: [4, 5],
    4: [],
    5: [],
    6: []
}

DFS(graph)
