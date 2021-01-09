from collections import defaultdict
from typing import DefaultDict

def topological_sort(graph, node):
    ret = []
    visited = set()

    def rec(node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                rec(neighbour)
        ret.insert(0, node) 
    # check all keys in graph are visited 
    for k in list(graph):
        if k not in visited:
            rec(k)
    return ret

if __name__ == '__main__':
    graph = defaultdict(set)  # string to set of strings 
    while True:
        edge = input("Enter an edge, eg.: A->B \n").strip().split("->")
        if len(edge) == 2:
            graph[edge[0]].add(edge[1])
        else:
            print("Directed graph constructed.")
            break 
    print("Topologically sorted: ", topological_sort(graph, next(iter(graph))))