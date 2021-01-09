## 2-opt TSP algorithm 

Input: weighted complete graph 

```
Enter the vertices separated by single comma: A,B,C,D,E
A | B | C | D | E
A-> 0,1,1,1,1 # enter the cost matrix as an adjacency matrix, separated by single comma 
B-> 1,0,1,1,1
C-> 1,1,0,1,1
D-> 1,1,1,0,1
E-> 1,1,1,1,0
```

Output: Hamiltonian cycle, with step-by-step swaps 

```
Tour: ['A', 'B', 'C', 'D', 'E'], total distance: 5
```

Procedure:

1. Construct Minimum Spanning Tree with Prim's algorithm.
2. Preorder traversal, and set the `score` to the weight sum. 
3. Heuristic: find the largest edge first, then other edges. 
    1. Choose another edge. 
    2. Cross: (a, b) with (c, d) --> (a,c)
    3. If total weight of new tour is smaller, update tour and start from 3 again. 