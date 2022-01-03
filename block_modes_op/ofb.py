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

def shift_left(m, n_bits):
    return m[n_bits:] + m[:n_bits]

def encrypt(m, k):
    # t = xor(m, k)
    return shift_left(m, 1)

# TODO: not tested
# For decryption, enter the ciphertext as the message
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CBC mode of operation for a custom cipher")
    # parser.add_argument("-v", action="store_true", help="Print intermediate steps")

    message = input("Input message: ")

    key = input("Input key: ")

    nonce = input("Input nonce: ")

    register = nonce

    output = ""

    for i in range((len(message) // len(key)) + 1):
        o = encrypt(register, key)
        register = o
        output += o
    output = output[:len(message)]

    print(f"Output: {output}")
    
    ciphertext = xor(message, output)
    print(f"Ciphertext: {ciphertext}")
