import argparse
import csv
from huntDT import * 

def main():
    parser = argparse.ArgumentParser(description="Hunt's algorithm walkthrough. By Roundofthree.")
    parser.add_argument("-v", action='store_true', help="Print the intermediate GINI indexes.")
    parser.add_argument("--table_csv", type=str, required=True, help="File path to a .csv file with the records.")
    arg = parser.parse_args()
    verbose = arg.v
    table_csv = arg.table_csv 
    records = []

    with open(table_csv, 'r') as f:
        f = csv.reader(f, delimiter=',')
        for line in f:
            r = [i for i in line]
            records.append(r)

    # n_records = len(records)
    # n_attributes = len(records[0]) - 1 # minus class column

    huntDT = HuntDT(records=records, verbose=verbose)
    root = huntDT.build()
    root.display() # display a tree with 
    # |-> (att_id: att_val) 
    #      |-> (att_id: att_val)


if __name__ == '__main__':
    main()
