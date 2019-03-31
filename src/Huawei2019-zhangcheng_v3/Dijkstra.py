import sys
import numpy


def dijkstra(graph, source, destination):
    vexnum = len(graph)
    #    pathMatrix = numpy.zeros([vexnum, vexnum])
    pre = numpy.zeros(vexnum)
    final = numpy.zeros(vexnum)
    distance = numpy.zeros(vexnum)
    for v in range(vexnum):
        final[v] = 0
        distance[v] = graph[source][v]
        #        for w in range(vexnum):
        #            pathMatrix[v][w] = 0
        #             pre[w] = -1
        if distance[v] < sys.maxsize:
            #            pathMatrix[v][source] = 1
            pre[v] = source
    #            pathMatrix[v][v]      = 1
    distance[source] = 0
    final[source] = 1

    for i in range(1, vexnum):
        min = sys.maxsize
        for w in range(vexnum):
            if final[w] == 0:
                if distance[w] < min:
                    v = w
                    min = distance[w]
        final[v] = 1
        for w in range(vexnum):
            if final[w] == 0 and min + graph[v][w] < distance[w]:
                distance[w] = min + graph[v][w]
                #               pathMatrix[w] = pathMatrix[v]
                #               pathMatrix[w][w] = 1
                pre[w] = v
    pre[source] = source
    path = []
    k = destination
    while k != source:
        k = int(k)
        '''
        if k == -1:
            path = []
            break
        '''
        path.append(k)
        k = pre[k]
    path.append(source)
    path.reverse()
    return path, distance[destination]
