## SAT solver

Arguments:
```
--mode, dpll or greedy (default)
```

Input:
```
Enter a clause, eg.: P,Q,-R
P,Q
Enter a clause, eg.: P,Q,-R
-Q
Enter a clause, eg.: P,Q,-R
-R
Enter a clause, eg.: P,Q,-R

Input finished.
```

Output:

For greedy mode:
```
Assignment:  {'R', 'P', 'Q'}
Score:  1
Change  R  to  -R
Assignment:  {'-R', 'P', 'Q'}
Score:  2
Change  -R  to  R
Change  P  to  -P
Change  Q  to  -Q
Assignment:  {'-R', 'P', '-Q'}
Score:  3
Change  -R  to  R
Change  P  to  -P
Change  -Q  to  Q
```

For DPLL mode:
```
Pure literal on  -R
Pure literal on  P
Unit propagation on  frozenset({'-Q'})
Solution:  -R P -Q
```

