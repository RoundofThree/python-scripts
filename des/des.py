def pad(block, p, bs):
    return block + p * (bs - len(block))

def split(m, bs):
    ret = []
    for i in range(len(m) // bs):
        ret.append(m[i*bs:(i+1)*bs])
    if len(m) % bs != 0:
        ret.append(pad(m[(len(m)//bs) * bs:], '0', bs))  # pad with 0
    return ret

def PC1(k):
    matrix = [57, 49, 41, 33, 25, 17, 9, 
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4]
    ret = list(len(matrix) * "0")
    for i in range(len(matrix)):
        ret[i] = k[matrix[i] - 1]  # convert to 0-indexed
    ret = ''.join(ret)
    return ret

def PC2(k):
    matrix = [14, 17, 11, 24, 1, 5, 3, 28,
     15, 6, 21, 10, 23, 19, 12, 4, 26,
      8, 16, 7, 27, 20, 13, 2, 41, 52,
       31, 37, 47, 55, 30, 40, 51, 45,
        33, 48, 44, 49, 39, 56, 34, 53,
         46, 42, 50, 36, 29, 32]
    ret = list(len(matrix) * "0")
    for i in range(len(matrix)):
        ret[i] = k[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def shift_left(m, n_bits):
    return m[n_bits:] + m[:n_bits]

def generate_subkeys(k):
    ret = []
    k = PC1(k) # 56-bit
    c, d = k[:28], k[28:]
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(16):
        c, d = shift_left(c, shift_table[i]), shift_left(d, shift_table[i])
        ret.append(PC2(c + d))
    return ret

def IP(m):
    ret = list(len(m) * "0")
    matrix = [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def E(m):
    matrix = [32,1,2,3,4,5,
        4,5,6,7,8,9,
        8,9,10,11,12,13,
        12,13,14,15,16,17,
        16,17,18,19,20,21,
        20,21,22,23,24,25,
        24,25,26,27,28,29,
        28,29,30,31,32,1]
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
    row = int(m[0] + m[5], 2)
    col = int(m[1:5], 2)
    ret = bin(box[row * 16 + col])[2:]
    ret = (4 - len(ret)) * "0" + ret
    return ret

def SBOX(m):
    # split into 6-bit blocks
    blocks = split(m, 6)
    ret = []
    S1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    S2 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    S3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    S4 = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    S5 = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    S6 = [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    S7 = [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    S8 = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ret.append(sbox(blocks[0], S1))
    ret.append(sbox(blocks[1], S2))
    ret.append(sbox(blocks[2], S3))
    ret.append(sbox(blocks[3], S4))
    ret.append(sbox(blocks[4], S5))
    ret.append(sbox(blocks[5], S6))
    ret.append(sbox(blocks[6], S7))
    ret.append(sbox(blocks[7], S8))
    return "".join(ret)

def P(m):
    ret = list(len(m) * "0")
    matrix = [16,7,20,21,29,12,28,17,
        1,15,23,26,5,18,31,10,
        2,8,24,14,32,27,3,9,
        19,13,30,6,22,11,4,25]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

def IPinv(m):
    ret = list(len(m) * "0")
    matrix = [40,8,48,16,56,24,64,32,
        39,7,47,15,55,23,63,31,
        38,6,46,14,54,22,62,30,
        37,5,45,13,53,21,61,29,
        36,4,44,12,52,20,60,28,
        35,3,43,11,51,19,59,27,
        34,2,42,10,50,18,58,26,
        33,1,41,9,49,17,57,25]
    for i in range(len(m)):
        ret[i] = m[matrix[i] - 1]
    ret = ''.join(ret)
    return ret

if __name__ == "__main__":
    message = input("Input message: ")
    assert len(message) == 64

    key = input("Input key: ")
    assert len(key) == 64

    decryption = input("Decryption? (y/n): ") == "y"

    # generate 16 subkeys
    subkeys = generate_subkeys(key)
    if decryption:
        subkeys = subkeys[::-1]

    # initial permutation
    message = IP(message)
    print(f"IP(M) = {message}")
    le, re = message[:32], message[32:]
    for i in range(16):
        round = i+1
        expanded = E(re)
        print(f"Round {round}")
        print(f"SubKey {round} = {subkeys[i]}")
        print(f"E(re) = {expanded}")
        xored = xor(expanded, subkeys[i])
        print(f"Xor(E(re), Ki) = {xored}")
        sboxed = SBOX(xored)
        print(f"SBOX(Xor(E(re), Ki)) = {sboxed}")
        permuted = P(sboxed)
        print(f"P(SBOX(Xor(E(re), Ki))) = {permuted}")

        le, re = re, xor(le, permuted)
        print(f"LE = {le}, RE = {re}")

        print("=========================")
    
    # swap (of Feistel)
    le, re = re, le
    # inverse initial permutation
    ciphertext = IPinv(le + re)
    print(f"IP-1({le + re}) = {ciphertext}")
