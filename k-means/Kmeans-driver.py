from Kmeans import *
import sys
import csv
import argparse

def main():
    parser = argparse.ArgumentParser(description="KMeans algorithm walkthrough. By Roundofthree.")
    parser.add_argument("--table_csv", type=str, required=True, help="File path to a .csv file with the records.")
    parser.add_argument("--metric", type=str, help="EUCLIDEAN or MANHATTAN")
    arg = parser.parse_args()
    table_csv = arg.table_csv 
    metric = arg.metric 
    records = []

    with open(table_csv, 'r') as f:
        f = csv.reader(f, delimiter=',')
        for line in f:
            r = [int(i) for i in line]
            records.append(r)

    n_records = len(records)
    n_attributes = len(records[0])
    # ask for k 
    k =  int(input("Enter k: "))
    while k > n_records:
        k = map(int, input(f"k must be <= than {n_records}"))
    # ask for k initial clusters
    print(f"Enter {k} points with {n_attributes}, each separated by a single comma:")
    centroids = []
    for i in range(k):
        input_array = list(map(int, input(str(i)+"-> ").strip().split(",")))
        while len(input_array) != n_attributes:
            input_array = list(map(int, input("Try again: "+i+"-> ").strip().split(",")))
        centroids.append(input_array)
    
    kmeans = KMeans(records=records, k=k, centroids=centroids, metric=metric)
    kmeans.print_table()
    while True:
        n_changes = kmeans.run_iteration()
        kmeans.print_table()
        if n_changes == 0: break
    

if __name__ == '__main__':
    main()
    