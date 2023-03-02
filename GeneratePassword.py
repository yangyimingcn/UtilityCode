import random


def print_letter_figure():
    n = 8  # 打印字符数
    sum_of_char = 62  # v中字符数
    v = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(n):
        x = random.randint(0, sum_of_char-1)
        if i != n-1:
            print(v[x], end=',')
        else:
            print(v[x])


def print_letter():
    n = 8
    sum_of_char = 52
    v = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
    for i in range(n):
        x = random.randint(0, sum_of_char-1)
        if i != n-1:
            print(v[x], end=',')
        else:
            print(v[x])


def print_figure_8():
    n = 8
    sum_of_char = 10
    v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(n):
        x = random.randint(0, sum_of_char-1)
        if i != n-1:
            print(v[x], end=',')
        else:
            print(v[x])


def print_figure_6():
    n = 6
    v = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sum_of_char = 10
    for i in range(n):
        x = random.randint(0, sum_of_char-1)
        if i != n-1:
            print(v[x], end=',')
        else:
            print(v[x])


def main():
    print_letter_figure()
    print_letter()
    print_figure_8()
    print_figure_6()


main()


