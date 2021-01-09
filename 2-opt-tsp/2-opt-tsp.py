import numpy as np

# convert A of input to 0, when output

class TSP:
    def __init__(self, weights, tour, verticesMapping):
        self.tour = tour  # preorder traversal of MST, ordered list of ints   
        self.weights = weights # np 2D array of ints, cost matrix, keys are ints  
        self.d = self.calculateWeight(tour)
        self.verticesMapping = verticesMapping
        print(f"Tour: {self.printTour(self.tour)}, total distance: {self.d}")
    
    # weight of the input tour 
    def calculateWeight(self, tour):
        ret = 0
        for idx in range(len(tour)):
            v_1 = tour[idx]
            if idx == len(tour)-1:
                v_2 = tour[0]
            else:
                v_2 = tour[idx+1]
            ret += self.weights[v_1][v_2]
        return ret

    # optimize 
    def optimize(self):
        N = len(self.tour)
        for i in range(N-3):
            for j in range(i+2, N-1):
                newTour = np.copy(self.tour)
                newTour[i+1] = self.tour[j]
                tmp = i+2
                for k in range(j-1, i, -1):
                    newTour[tmp] = self.tour[k]
                    tmp += 1
                newD = self.calculateWeight(newTour)
                if newD < self.d:
                    self.tour = np.copy(newTour)
                    self.d = newD
                    print(f"Tour: {self.printTour(self.tour)}, total distance: {self.d}")
                    self.optimize()  # tail recursive 

    # map a list of integers to the corresponding list of strings 
    def printTour(self, tour):
        return list(map(lambda x: self.verticesMapping[x], tour))
from collections import defaultdict
from typing import DefaultDict
import heapq
class MST:
    def __init__(self, cost, root):
        self.root = root 
        self.cost_matrix = cost 
        self.mst = self.prims()

    def prims(self):
        ret = defaultdict(set) 
        visited = set([self.root])
        edges = [(cost, self.root, v_2) for v_2, cost in enumerate(self.cost_matrix[self.root])]
        heapq.heapify(edges)
        while edges:
            cost, start, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                ret[start].add(to) 
                for to_next, cost in enumerate(self.cost_matrix[to]):
                    if to_next not in visited:
                        heapq.heappush(edges, (self.cost_matrix[to][to_next], to, to_next))
        return ret

    def preorder(self, root):
        # convert mst a dictionary to list 
        children = self.mst[root]
        ret = [root]
        for child in children:
            ret = ret + self.preorder(child)
        return ret 

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Apply 2-opt algorithm to approximate TSP solution step by step. By Roundofthree.")
    # ask for vertices, eg.: A,B,C,D,E
    vertices = input("Enter the vertices separated by single comma: ").strip().split(",")  # ['A', 'B', 'C', 'D', 'E']
    verticesMapping = []
    N = len(vertices)
    for i in range(0, N):
        verticesMapping.append(vertices[i]) 
    # ask for cost matrix nxn, eg.:
    #  A | B | C | D | E
    # A -> 0,13,23,4,2,4
    # B -> 
    print(' | '.join(vertices))
    cost = [] 
    for v in vertices:
        input_array = list(map(int, input(v+"-> ").strip().split(",")))
        if len(input_array) == N:
            cost.append(input_array)
        else: 
            print("error") # and terminate 
    np_cost = np.array(cost).reshape(N,N)
    # calculate MST from np_cost and vertices --> Prim's starting from 0 
    mst = MST(np_cost, 0) 
    mst_preorder = mst.preorder(0) 
    # mst_preorder = [0, 1, 2, 3, 4] 
    # compute preorder traversal of tree as a list 
    tsp_solver = TSP(np_cost, mst_preorder, verticesMapping)
    tsp_solver.optimize()
    

        

    
        