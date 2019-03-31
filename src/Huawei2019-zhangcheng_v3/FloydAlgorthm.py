import numpy
import sys

def Floyd(graph):

    vexnum = len(graph)
    P = numpy.zeros((vexnum, vexnum))
    D = numpy.zeros((vexnum, vexnum))

    for i in range(vexnum):
        for j in range(vexnum):
           D[i][j] = graph[i][j]
           if graph[i][j] < sys.maxsize:
               P[i][j] = i
           else:
               P[i][j] = -1

    for k in range(vexnum):
        for i in range(vexnum):
            for j in range(vexnum):
                if  D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]

    return P, D
