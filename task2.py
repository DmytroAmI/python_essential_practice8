def read_gen(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


if __name__ == '__main__':
    read_file = read_gen("task1.txt")
    for text in read_file:
        print(text)
