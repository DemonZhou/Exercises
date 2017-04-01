# -*- coding: utf-8 -*-  
class Quene:
    def __init__(self):
        self.quene = []

    def enquene(self, x):
        self.quene.append(x)

    def dequene(self):
        if self.isEmpty():
            return None
        x = self.quene[0]
        self.quene.pop(0)
        return x

    def isEmpty(self):
        return len(self.quene) == 0


def BFS(graph, vstart):
    quene = Quene()
    vlist = []
    vlist.append(vstart)
    quene.enquene(vstart)
    while not quene.isEmpty():
        u = quene.dequene()
        for v in graph[u]:
            if v not in vlist:
                vlist.append(v)
                print vlist #显示搜索过程
                quene.enquene(v)


graph = {
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: []
}

BFS(graph, 1)
