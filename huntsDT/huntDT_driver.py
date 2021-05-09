import argparse
from huntDS import * 

def main():
    parser = argparse.ArgumentParser(description="Hunt's algorithm walkthrough. By Roundofthree.")
    parser.add_argument("-v", action='store_true', help="Print the intermediate GINI indexes.")
    parser.add_argument("--table_csv", type=str, help="File path to a .csv file with the records.")
    arg = parser.parse_args()
    verbose = arg.v   

if __name__ == '__main__':
    main()
