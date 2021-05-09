from Kmeans import *
import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("\nError")
        print("\nUsage: > Kmeans-driver.py <table.csv>")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    records = []

    with open(input_file, 'r') as f:
        f = csv.reader(f, delimiter=',')
        for line in f:
            r = [int(i) for i in line]
            records.append(r)

    n_records = len(records)
    n_attributes = len(records[0])
    # ask for k 
    k = map(int, input("Enter k: "))
    while k > n_records:
        k = map(int, input(f"k must be <= than {n_records}"))
    # ask for k initial clusters
    print(f"Enter {k} points with {n_attributes}, each separated by a single comma:")
    centroids = []
    for i in range(k):
        input_array = list(map(int, input(k+"-> ").strip().split(",")))
        while len(input_array) != n_attributes:
            input_array = list(map(int, input("Try again: "+k+"-> ").strip().split(",")))
        centroids.append(input_array)
    
    kmeans = KMeans(records=records, k=k, centroids=centroids)
    while True:
        n_changes = kmeans.run_iteration()
        kmeans.print_table()
        if n_changes == 0: break
    

if __name__ == '__main__':
    main()
    