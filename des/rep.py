if __name__ == "__main__":
    with open("test", "r") as f:
        c = f.read()
        c = c.replace(" ", "").replace("\n", "")
        print(c)