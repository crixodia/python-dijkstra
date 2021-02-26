# -*- coding: utf-8 -*-
# Author: Cristian Bastidas
# GitHub: https://github.com/crixodia
# Date: 2020-10-7

from graphviz import Graph


def undirected_graph(wmat, name="weighted_undirected_graph"):
    """
    Creates a pdf file with a weigthted graph's visualization

    You must have installed graphviz (Python conector and OS compilation)
      OS: https://www.graphviz.org/
      Python module: https://graphviz.readthedocs.io/en/stable/index.html

    Args:
    wmat  --  weigthted graph's adjacency matrix
    name  --  (optional) graph's filename
    """
    n = len(wmat)
    f = Graph(name, filename=name+'.gv')
    f.attr('node', shape='circle')
    for i in range(n):
        f.node(str(i))

    for i in range(n):
        for j in range(n):
            if wmat[i][j] != 0 and i < j:
                f.edge(str(i), str(j), label=str(wmat[i][j]))

    return f.view()
