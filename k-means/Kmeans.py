import numpy as np
from math import sqrt

# Euclid distance
def euclid(a, b):
    if len(a) != len(b): return
    n = len(a)
    ret = 0
    for i in range(n):
        ret += (a[i]-b[i])**2
    return sqrt(ret)

# Manhattan distance
def manhattan(a, b):
    if len(a) != len(b): return # raise error 
    n = len(a)
    ret = 0
    for i in range(n):
        ret += abs(a[i] - b[i])
    return ret

class KMeans:
    def __init__(self, records=[], k=0, centroids=[], metric="EUCLIDEAN"):
        self.iteration_n = 1
        self.records = records
        self.k = k
        self.centroids = centroids
        if metric == "EUCLIDEAN":
            self.distance = euclid
        else:  # metric == "MANHATTAN"
            self.distance = manhattan
        for r in records:
            r.append(0)  # cluster id col 

    def run_iteration(self):
        self.iteration_n += 1
        # print(f"Iteration {self.iteration_n}")
        # for each point, compute the distance to each of the centroids 
        for p in self.records:
            min_d = np.inf 
            chosen = 0
            for i in range(len(self.centroids)):
                d = self.distance(p[:-1], self.centroids[i])
                if d < min_d:
                    min_d = d 
                    chosen = i
            p[-1] = chosen
        # compute the mean k clusters
        n_sum = [0 for i in range(len(self.centroids))]
        cummulative_sum = [[0 for j in range(len(self.centroids[0]))] for i in range(len(self.centroids))]
        for p in self.records:
            for i in range(len(p)-1):
                # update 
                cummulative_sum[p[-1]][i] += p[i]
            n_sum[p[-1]] += 1
        n_changes = 0
        for i in range(len(self.centroids)):
            c = self.centroids[i]
            for j in range(len(c)):
                old = c[j]
                c[j] = cummulative_sum[i][j] / n_sum[i]
                # print(f"cummulative sum of centroid {i} is {cummulative_sum[i][j]}")
                if old != c[j]:
                    n_changes += 1 
        return n_changes
    
    def print_table(self):
        # print(len(self.records))
        print(f"Iteration {self.iteration_n}")
        print()
        for i in range(len(self.centroids)):
            out = f"C{i}: "
            c = self.centroids[i]
            out += "(" + ", ".join(str(j) for j in c) + ")"
            print(out)
        for r in self.records:
            out = "(" + ", ".join(str(i) for i in r[:-1]) + ") -> "
            for c in self.centroids:
                out += str(self.distance(r[:-1], c))
                out += " | "
            out += "Cluster "
            out += str(r[-1])
            print(out)
