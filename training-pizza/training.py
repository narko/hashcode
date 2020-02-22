import sys
import numpy


def read_input(file_name):
    with open(file_name, 'r') as file:
        m, n = file.readline().split(' ')
        print(m, n)
        s = [int(x) for x in file.readline().strip('\n').split(' ')]
        print(s)
        return [int(m), int(n), s]


def write_ouput(data):
    with open('e-out.txt', 'w') as file:
        file.write('{}\n'.format(len(data)))
        file.write(' '.join(map(str, data)))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: ./main.py FILE")
        sys.exit(1)

    score = 0

    total_slices, pizza_types, pizza_slices = read_input(sys.argv[1])

    pizzas = numpy.zeros(pizza_types)

    for i, item in enumerate(reversed(pizza_slices)):
        if (score + item <= total_slices):
            pizzas[i] = 1
            score += item

    x = [a for a, b in enumerate(reversed(pizzas)) if b == 1.0]
    write_ouput(x)

