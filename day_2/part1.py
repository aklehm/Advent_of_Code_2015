def calcArea(length: int, width: int, height: int) -> int:
    lw = length*width
    lh = length*height
    wh = width*height

    minArea = min(lw, lh, wh)

    return 2*lw + 2*lh + 2*wh + minArea


def main():
    rawlines = list()

    with open('./day_2/input.txt', 'r') as f:
        rawlines = f.readlines()

    totalPaper = 0
    for line in rawlines:
        # print(line)
        box = line.split('x')
        totalPaper = totalPaper + calcArea(length=int(box[0]), width=int(box[1]), height=int(box[2]))

    print(f'Needed paper: {totalPaper}')


if __name__ == '__main__':
    main()
