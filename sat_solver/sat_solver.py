def score(clauses, assignment):
    ret = 0
    for c in clauses:
        satisfied = False
        for v in c: 
            if v in assignment:
                satisfied = True
                break 
        if satisfied:
            ret += 1
    return ret 

def opposite(var):
    if var.startswith('-'):
        return var[1:]
    else:
        return '-' + var 

def greedy_rec(clauses, curr_score, assignment):
    print("Assignment: ", assignment)
    print("Score: ", curr_score)
    if score == len(assignment): 
        return 
    for var in assignment:
        print("Change ", var, " to ", opposite(var))
        assignment.remove(var)
        assignment.add(opposite(var))
        new_score = score(clauses, assignment)
        if new_score > curr_score:
            greedy_rec(clauses, new_score, assignment)
            break
        else:
            assignment.remove(opposite(var))
            assignment.add(var)

# print assignment and score in each iteration 
def greedy_solve(clauses):
    ret = set() # U 
    # fill in all vars in clauses  
    for c in clauses:
        for n in c:
            ret.add(n.replace("-", ""))
    curr_score = score(clauses, ret) 
    # iterate
    return greedy_rec(clauses, curr_score, ret)

# DPLL -----------------
import random 

def get_counter(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter

def bcp(formula, unit):
    modified = set()
    for clause in formula:
        if unit in clause: continue
        tmp = opposite(unit)
        if tmp in clause:
            c = frozenset([x for x in clause if x != tmp])
            if len(c) == 0: return -1
            modified.add(c)
        else:
            modified.add(clause)
    return modified

def pure_literal(formula):
    counter = get_counter(formula)
    assignment = []
    pures = [] 
    for literal, times in counter.items():
        if opposite(literal) not in counter: pures.append(literal)
    for pure in pures:
        print("Pure literal on ", pure)
        formula = bcp(formula, pure)
    assignment += pures
    return formula, assignment

def unit_propagation(formula):
    assignment = []
    unit_clauses = [c for c in formula if len(c) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        print("Unit propagation on ", unit)
        formula = bcp(formula, next(iter(unit)))
        assignment += [next(iter(unit))]
        if formula == -1:
            return -1, []
        if not formula:
            return formula, assignment
        unit_clauses = [c for c in formula if len(c) == 1]
    return formula, assignment

def variable_selection(formula):
    counter = get_counter(formula)
    return random.choice(list(counter))

def backtracking(formula, assignment):
    formula, pure_assignment = pure_literal(formula)
    formula, unit_assignment = unit_propagation(formula)
    assignment = assignment + pure_assignment + unit_assignment
    if formula == - 1:
        print("Unsatisfiable")
        return []
    if not formula:
        print("Solution: ", ' '.join(assignment))  # possible double output 
        return assignment

    variable = variable_selection(formula)
    print("Branch on ", variable)
    solution = backtracking(bcp(formula, variable), assignment + [variable])
    if not solution:
        print("Conflict, backtrack to ", opposite(variable))
        solution = backtracking(bcp(formula, opposite(variable)), assignment + [opposite(variable)])
    if solution: print("Solution: ", ' '.join(solution))
    else: print("Unsatisfiable")
    return solution 

def dpll_solve(clauses): 
     backtracking(clauses, [])

def sat_solve(clauses, mode):
    if mode == "greedy":
        greedy_solve(clauses)
    elif mode == "dpll":
        dpll_solve(clauses)
    else:
        greedy_solve(clauses)

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple SAT solver. By Roundofthree.")
    parser.add_argument("--mode", type=str, help="Use 'greedy' or 'dpll'. Default is dpll.")
    arg = parser.parse_args()
    mode = arg.mode # 'greedy' or 'dpll'  
    clauses = set()
    while True:
        clause = frozenset(input("Enter a clause, eg.: P,Q,-R \n").strip().split(","))
        if next(iter(clause)) == '':
            print("Input finished.")
            break 
        clauses.add(clause)  
    sat_solve(clauses, mode)

    
