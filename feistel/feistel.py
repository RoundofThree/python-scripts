import argparse

# a and b are strings of 0 and 1
def xor(a, b):
    n = len(a)
    c = ""
    for i in range(n):
        if ord(a[i]) ^ ord(b[i]) == 0:
            c += '0'
        else:
            c += '1'
    return c

# xor
def round_function(block, subkey):
    return xor(block, subkey)

# split key into 3 blocks
def subkey_generator(key, round):
    length = len(key) // 3  # change number of blocks here
    start = (round - 1) * length
    end = round * length
    return key[start:end]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Feistel cipher. By Roundofthree.")
    parser.add_argument("-v", action='store_true', help="Print intermediate steps")
    arg = parser.parse_args()
    verbose = arg.v

    # prompt for message input
    message = input("Input message: ")
    mid = len(message) // 2
    le, re = message[:mid], message[mid:]

    # prompt for key input
    key = input("Input key: ")
    
    n_rounds = 3 # number of rounds
    for round in range(1, n_rounds+1):
        subkey = subkey_generator(key, round)
        le, re = re, xor(le, round_function(re, subkey)) # updated simultaneously
        if verbose:
            print(f"LE {round} = {le}")
            print(f"RE {round} = {re}")
            print(f"Subkey used is {subkey}")
            print()

    # w-bit swap
    le, re = re, le
    print(f"LE_{n_rounds + 1} = {le}")
    print(f"RE_{n_rounds + 1} = {re}")
    