# -*- coding: utf-8 -*-
import sys
vertexs = set(['a','b','c','d','e','f','g','h','i'])

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

def MST_Prim(vertexs,edges):
    Vnew = set()
    Enew = []
    tmp = vertexs.pop()
    Vnew.add(tmp)
    vertexs.add(tmp)
    length = 0
    while Vnew != vertexs:
        min = sys.maxint
        u = None
        v = None
        for item in edges:
            if item[2] < min:
                if item[0] in Vnew and item[1] not in Vnew:
                    min = item[2]
                    u = item[0]
                    v = item[1]
                elif item[1] in Vnew and item[0] not in Vnew:
                    min = item[2]
                    u = item[1]
                    v = item[0]
        if u != None and v != None:
            Enew.append(set([u,v,min]))
            length += min
            Vnew.add(v)
    print length

MST_Prim(vertexs,edges)