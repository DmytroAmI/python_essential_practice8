def add(filename, content):
    with open(filename, "a") as file:
        file.write(content)


def read(filename):
    with open(filename, "r") as file:
        print(file.read())


if __name__ == "__main__":
    add('task1.txt', 'hello world\n')
    add('task1.txt', 'how are you\n')

    read('task1.txt')
