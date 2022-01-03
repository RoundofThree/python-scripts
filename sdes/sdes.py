def pad(block, p, bs):
    return block + p * (bs - len(block))

def split(m, bs):
    ret = []
    for i in range(len(m) // bs):
        ret.append(m[i*bs:(i+1)*bs])
    if len(m) % bs != 0:
        ret.append(pad(m[(len(m)//bs) * bs:], '0', bs))  # pad with 0
    return ret

def P10(k):
    matrix = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    ret = list(len(matrix) * "0")
    for i in range(len(matrix)):
        ret[i] = k[matrix[i] - 1]  # convert to 0-indexed
    ret = ''.join(ret)
    return ret

def P8(k):
    matrix = [6, 3, 7, 4, 8, 5, 10, 9]
    ret = list(len(matrix) * "0")
    for i in range(len(matrix)):
        ret[i] = k[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def shift_left(m, n_bits):
    return m[n_bits:] + m[:n_bits]

def generate_subkeys(k):
    ret = []
    k = P10(k)
    c, d = k[:5], k[5:]
    shift_table = [1, 2]
    for i in range(2):
        c, d = shift_left(c, shift_table[i]), shift_left(d, shift_table[i])
        ret.append(P8(c + d))
    return ret

def IP(m):
    ret = list(len(m) * "0")
    matrix = [2, 6, 3, 1, 4, 8, 5, 7]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def E(m):
    matrix = [4, 1, 2, 3, 2, 3, 4, 1]
    ret = list(len(matrix) * "0")
    for i in range(len(matrix)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
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

def sbox(m, box):
    row = int(m[0] + m[3], 2)
    col = int(m[1:3], 2)
    ret = bin(box[row * 4 + col])[2:]
    ret = (2 - len(ret)) * "0" + ret
    return ret

def SBOX(m):
    # split into 6-bit blocks
    blocks = split(m, 4)
    ret = []
    S1 = [1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2]
    S2 = [0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3]
    ret.append(sbox(blocks[0], S1))
    ret.append(sbox(blocks[1], S2))
    return "".join(ret)

def P4(m):
    ret = list(len(m) * "0")
    matrix = [2, 4, 3, 1]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def IPinv(m):
    ret = list(len(m) * "0")
    matrix = [4, 1, 3, 5, 7, 2, 8, 6]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

if __name__ == "__main__":
    message = input("Input message: ")
    assert len(message) == 8

    key = input("Input key: ")
    assert len(key) == 10

    decryption = input("Decryption? (y/n): ") == "y"

    # generate 2 subkeys
    subkeys = generate_subkeys(key)
    if decryption: subkeys = subkeys[::-1]

    # initial permutation
    message = IP(message)
    print(f"IP(M) = {message}")
    le, re = message[:4], message[4:]
    for i in range(2):
        round = i+1
        expanded = E(re)
        print(f"Round {round}")
        print(f"SubKey {round} = {subkeys[i]}")
        print(f"E(re) = {expanded}")
        xored = xor(expanded, subkeys[i])
        print(f"Xor(E(re), Ki) = {xored}")
        sboxed = SBOX(xored)
        print(f"SBOX(Xor(E(re), Ki)) = {sboxed}")
        permuted = P4(sboxed)
        print(f"P4(SBOX(Xor(E(re), Ki))) = {permuted}")

        if round == 1:
            le, re = re, xor(le, permuted)  # swap
        else:
            le, re = xor(le, permuted), re
        
        print(f"LE = {le}, RE = {re}")

        print("=========================")
    
    # no swap (of Feistel)
    # inverse initial permutation
    ciphertext = IPinv(le + re)
    print(f"IP-1({le + re}) = {ciphertext}")
