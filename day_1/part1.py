def main():
    rawlines = list()

    with open('./day_1/input.txt', 'r') as f:
        rawlines = f.readlines()

    floor = 0

    for c in rawlines[0]:
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1

    print(f'Floor: {floor}')


if __name__ == '__main__':
    main()
