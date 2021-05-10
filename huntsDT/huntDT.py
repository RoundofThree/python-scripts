import numpy as np 


class Node:
    def __init__(self, records, visited=None):
        self.records = records 
        self.attribute_id = 0 
        self.attribute_val = None 
        self.children = []
        self.visited = visited or [False for i in range(len(records)-1)]

    def set_attribute(self, att_id, att_val):
        self.attribute_id = att_id
        self.attribute_val = att_val

    def add_child(self, node):
        self.children.append(node)

    def display(self, level=0):
        out = level * 5 * ' '
        out += f"|-> ({self.attribute_id}: {self.attribute_val})"
        out += "\n"
        print(out)
        for child in self.children:
            child.display(level=level+1) 
    

class HuntDT:
    def __init__(self, records=[], verbose=False):
        self.records = records 
        self.verbose = verbose
        # build domain of each attribute: att id -> list of str 
        self.domains = [self.domain(i) for i in range(len(records[0]))]

    # return set of different values the attribute can take 
    def domain(self, att_id):
        s = set()
        for r in self.records:
            s.add(r[att_id])
        return s

    # build tree
    def build(self):
        root = Node(self.records)
        root = self.build_tree(root)
        return root 

    def build_tree(self, node, level=0):
        split_att = self.select(node, level)
        if split_att == -1: return node 
        visited = node.visited.copy() 
        visited[split_att] = True 
        for val in self.domains[split_att]:
            group = filter(lambda r: r[split_att]==val, node.records)
            child = Node(list(group), visited=visited) 
            child.set_attribute(split_att, val)
            node.add_child(self.build_tree(child, level+1))
        return node 

    # select based on gini split index 
    def select(self, node, level=0):
        records = node.records
        if len(records) == 0: return -1
        min_gini = np.inf 
        chosen = -1 
        for att_id in range(len(self.domains)-1):
            if node.visited[att_id]: continue 
            gini = self.gini_index(records, att_id)
            if self.verbose:
                margin = level * 5 * ' '
                # print(f"{margin}At state {node.visited}")
                print(f"{margin}Gini split for {att_id}: {gini}")
            if gini < min_gini:
                min_gini = gini 
                chosen = att_id 
        if chosen != -1 and self.verbose: print(f"{level*5*' '}Choose att {chosen}")
        else:
            # find the frequency of classes 
            for class_id in self.domains[-1]:
                count = len(list(filter(lambda r: r[-1]==class_id, records)))
                child = Node(records)
                child.set_attribute(class_id, count)
                node.add_child(child)
        return chosen

    def gini_index(self, records, split_att_id):
        n_records = len(records)
        gini = 0.0
        # split records by attribute 
        for val in self.domains[split_att_id]:
            group = list(filter(lambda r: r[split_att_id]==val, records))
            if len(group) == 0:
                continue 
            squared_sum = 0.0
            classes = [r[-1] for r in group]
            for class_id in self.domains[-1]:
                p = classes.count(class_id) / len(group)
                squared_sum += p * p 
            gini += (1.0 - squared_sum) * (len(group)/n_records)
        return gini 

