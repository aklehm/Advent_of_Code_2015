'''
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
'''


def main():
    rawlines = list()

    with open('./day_3/input.txt', 'r') as f:
        rawlines = f.readlines()

    directions = rawlines[0]
    visitedHouses = 1
    curPosSanta = [1, 1]
    curPosRoboSanta = [1, 1]
    visitedPositions = ['1,1']

    print(len(directions))

    for i in range(len(directions)):
        d = directions[i]
        if i % 2 == 0:
            # Robo Santa
            x = curPosRoboSanta[0]
            y = curPosRoboSanta[1]
        else:
            # Human Santa
            x = curPosSanta[0]
            y = curPosSanta[1]

        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '<':
            x -= 1
        elif d == '>':
            x += 1

        newPosition = [x, y]
        newPosStr = f'{x},{y}'

        if newPosStr not in visitedPositions:
            visitedPositions.append(newPosStr)
            visitedHouses += 1

        if i % 2 == 0:
            # Robo Santa
            curPosRoboSanta = newPosition
        else:
            # Human Santa
            curPosSanta = newPosition

    print(f'Visited houses: {visitedHouses}')


if __name__ == '__main__':
    main()
