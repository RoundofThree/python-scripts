import numpy as np 

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
    def __init__(self, records=[], k=0, centroids=[], metric="EUCLID"):
        self.iteration_n = 1
        self.records = records
        self.k = k
        self.centroids = centroids
        if metric == "EUCLID":
            self.distance = euclid
        else:
            self.distance = manhattan
        for r in records:
            r.append(0)  # cluster id col 

    def run_iteration(self):
        # print(f"Iteration {self.iteration_n}")
        # for each point, compute the distance to each of the centroids 
        # hard coded Euclidean distance 
        for p in records:
            min_d = np.inf 
            chosen = 0
            for i in range(len(centroids)):
                d = self.distance(p[:-1], centroids[i])
                if d < min_d:
                    min_d = d 
                    chosen = i
            p[-1] = chosen
        # compute the mean k clusters
        n_sum = [0 for i in range(len(centroids))]
        cummulative_sum = [[0 for j in range(len(centroids[0]))] for i in range(len(centroids))]
        for p in records:
            for i in range(len(p)):
                # update 
                cummulative_sum[p[-1]][i] += p[i]
                n_sum[p[-1]] += 1
        for i in range(len(centroids)):
            c = centroids[i]
            for j in range(len(c)):
                c[j] = cummulative_sum[i][j] / n_sum[i]
    
    def print_table(self):
        for r in records:
            out = "(" + ", ".join(r[:-1]) + ")"
            out + " -> "
            for c in centroids:
                out += self.distance(r[:-1], c)
                out += " | "
            out += "Cluster "
            out += r[-1]
