# -*- coding: utf-8 -*-  
setlist = []


def Union(u,v):
    i = 0
    j = 0
    for i in range(0,len(setlist)):
        if u in setlist[i]:
            break
    for j in range(0,len(setlist)):
        if v in setlist[j]:
            break
    if i == j:
        return
    setlist[i] = setlist[i].union(setlist[j])
    setlist[j].clear()
    

def Make_Set(v):
    for item in setlist:
        if v in item:
            return
    vset = set()
    vset.add(v)
    setlist.append(vset)

def Find_Set(u):
    i = -1
    for i in range(0,len(setlist)):
        if u in setlist[i]:
            break
    return i

def MST_Kruskal(edges):
    length  = 0
    for item in edges:
        Make_Set(item[0])
        Make_Set(item[1])
    edges = sorted(edges,key=lambda a:a[2])
    for E in edges:
        if Find_Set(E[0]) != Find_Set(E[1]):
            Union(E[0],E[1])
            length += E[2]
    return length




edges = [
    ('a','b',4),
    ('a','h',8),
    ('b','h',11),
    ('b','c',8),
    ('c','d',7),
    ('c','i',2),
    ('c','f',4),
    ('d','e',9),
    ('d','f',14),
    ('e','f',10),
    ('f','g',2),
    ('g','h',1),
    ('g','i',6),
    ('h','i',7)
]

print MST_Kruskal(edges)