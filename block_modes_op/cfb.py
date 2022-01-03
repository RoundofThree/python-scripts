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

def msb(block, s):
    return block[:s]

def shift_left(m, n_bits):
    return m[n_bits:] + m[:n_bits]

def encrypt(m, k):
    # t = xor(m, k)
    return shift_left(m, 1)

# not tested yet TODO
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CBC mode of operation for a custom cipher")
    parser.add_argument("-d", action="store_true", help="Set decryption mode")
    arg = parser.parse_args()
    decryption = arg.d
    # parser.add_argument("-v", action="store_true", help="Print intermediate steps")

    block_size = int(input("Input block size: "))
    segment_size = int(input("Input segment size: "))
    message = input("Input message/ciphertext: ")
    blocks = split(message, segment_size)

    key = input("Input key: ") # has block size

    iv = input("Input IV: ") # has block size

    register = iv # has block size

    for block in blocks:
        t = encrypt(register, key)
        c = xor(block, msb(t, segment_size))
        print(c)
        if decryption: register = register[segment_size:] + block
        else: register = register[segment_size:] + c
