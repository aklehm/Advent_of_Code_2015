def main():
    rawlines = list()

    with open('./day_1/input.txt', 'r') as f:
        rawlines = f.readlines()

    floor = 0
    position = 0

    for c in rawlines[0]:
        position += 1
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1
        if floor == -1:
            break

    print(f'Floor: {floor}')
    print(f'Position: {position}')


if __name__ == '__main__':
    main()
