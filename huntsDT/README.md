# Hunt's algorithm to build Decision Trees 

Build a Decision Tree by splitting based on GINI index. Also outputs the GINI values to explain why the algo chose some attribute. 

## Example 

Input:

*Note*: The last column must be the class identifier

```bash
python3 huntDT_driver.py -v --table_csv table.csv
```

Output:

*Note*: Each node in the tree is represented as (attribute column number that this node was previously splitted: attribute value). That's why the root node is always (0: None). 

```
Gini split for 0: 0.48
Gini split for 1: 0.16250000000000003
Gini split for 2: 0.4789285714285715
Choose att 1
     Gini split for 0: 0.375
     Gini split for 2: 0.0
     Choose att 2
          Gini split for 0: 0.0
          Choose att 0
          Gini split for 0: 0.0
          Choose att 0
          Gini split for 0: 0.0
          Choose att 0
     Gini split for 0: 0.21428571428571433
     Gini split for 2: 0.16666666666666666
     Choose att 2
          Gini split for 0: 0.3333333333333333
          Choose att 0
          Gini split for 0: 0.0
          Choose att 0
          Gini split for 0: 0.0
          Choose att 0
     Gini split for 0: 0.0
     Gini split for 2: 0.0
     Choose att 0
          Gini split for 2: 0.0
          Choose att 2
          Gini split for 2: 0.0
          Choose att 2
|-> (0: None)

     |-> (1: High)

          |-> (2: Poor)

               |-> (0: F)

               |-> (0: M)

                    |-> (B: 1)

                    |-> (A: 0)

          |-> (2: Fair)

               |-> (0: F)

               |-> (0: M)

                    |-> (B: 0)

                    |-> (A: 1)

          |-> (2: Excellent)

               |-> (0: F)

               |-> (0: M)

                    |-> (B: 2)

                    |-> (A: 0)

     |-> (1: Low)

          |-> (2: Poor)

               |-> (0: F)

                    |-> (B: 1)

                    |-> (A: 1)

               |-> (0: M)

                    |-> (B: 1)

                    |-> (A: 0)

          |-> (2: Fair)

               |-> (0: F)

                    |-> (B: 2)

                    |-> (A: 0)

               |-> (0: M)

          |-> (2: Excellent)

               |-> (0: F)

                    |-> (B: 3)

                    |-> (A: 0)

               |-> (0: M)

     |-> (1: Medium)

          |-> (0: F)

               |-> (2: Poor)

               |-> (2: Fair)

                    |-> (B: 0)

                    |-> (A: 2)

               |-> (2: Excellent)

                    |-> (B: 0)

                    |-> (A: 1)

          |-> (0: M)

               |-> (2: Poor)

                    |-> (B: 0)

                    |-> (A: 3)

               |-> (2: Fair)

               |-> (2: Excellent)

                    |-> (B: 0)

                    |-> (A: 2)
```
