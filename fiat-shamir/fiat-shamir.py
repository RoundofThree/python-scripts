import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simulation of Fiat-Shamir protocol. By RoundofThree")
    parser.add_argument("--cheat", action="store_true", help="Show cheat strategy")
    arg = parser.parse_args()
    cheat = arg.cheat

    p = int(input("p: "))
    q = int(input("q: "))
    n = p * q

    s = int(input("Secret s: "))
    v = pow(s, 2, n)
    print(f"v is {v}")

    r = int(input("Commitment r: "))

    x = 0
    if not cheat:
        x = pow(r, 2, n)
    else:
        guess = int(input("Challenge guess by Pamela: "))
        if guess == 1: x = (pow(r, 2, n) * pow(v, -1, n)) % n
        elif guess == 0: x = pow(r, 2, n)
    print(f"x is {x}")

    c = int(input("Challenge c: "))

    y = 0
    if not cheat:
        y = (r * pow(s, c, n)) % n
    else:
        y = r % n
    print(f"y is {y}")

    y2 = pow(y, 2, n)
    print(f"y2 is {y2}")

    xv = (x * pow(v, c, n)) % n
    print(f"(x * v^c) % n = {xv}")
