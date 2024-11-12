'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio
and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
'''


def main():
    rawlines = list()

    with open('./day_3/input.txt', 'r') as f:
        rawlines = f.readlines()

    directions = rawlines[0]
    visitedHouses = 1
    currentPosition = [1, 1]
    visitedPositions = ['1,1']

    print(len(directions))

    for d in directions:
        x = currentPosition[0]
        y = currentPosition[1]

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

        currentPosition = newPosition

    print(f'Visited houses: {visitedHouses}')


if __name__ == '__main__':
    main()
