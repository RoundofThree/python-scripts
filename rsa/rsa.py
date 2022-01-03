import argparse
import math

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA simulation. By RoundofThree")
    parser.add_argument("--decrypt", action="store_true", help="Set decryption mode")
    arg = parser.parse_args()
    decryption = arg.decrypt

    p = int(input("p: "))
    q = int(input("q: "))
    n = p * q
    fi = (p-1) * (q-1)
    print(f"fi(n) is {fi}")

    e = int(input("Choose e: "))
    if math.gcd(e, fi) != 1:
        print("Invalid!")
        exit(-1)

    # calculate d
    d = pow(e, -1, fi)
    print(f"d is {d}")

    message = int(input("Plaintext/Ciphertext: "))

    # encrypt 
    if not decryption:
        c = pow(message, e, n)
        print(f"Ciphertext is {c}")
    else:
    # decrypt
        p = pow(message, d, n)
        print(f"Plaintext is {p}")
