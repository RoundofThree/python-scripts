import argparse

def pad(block, p, bs):
    return block + p * (bs - len(block))

def split(m, bs):
    ret = []
    for i in range(len(m) // bs):
        ret.append(m[i*bs:(i+1)*bs])
    if len(m) % bs != 0:
        ret.append(pad(m[(len(m)//bs) * bs:], '0', bs))  # pad with 0
    return ret

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

def shift_left(m, n_bits):
    return m[n_bits:] + m[:n_bits]

def shift_right(m, n_bits):
    rest = len(m) - n_bits
    return m[rest:] + m[:rest]

def encrypt(m, k):
    return shift_left(m, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ECB mode of operation for a custom cipher")
    # parser.add_argument("-v", action="store_true", help="Print intermediate steps")

    block_size = int(input("Input block size: "))
    message = input("Input message: ")
    blocks = split(message, block_size)

    key = input("Input key: ")

    for block in blocks:
        c = encrypt(block, key)
        print(c)
