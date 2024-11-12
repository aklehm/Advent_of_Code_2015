
def checkNice(string: str) -> bool:
    notAllowed = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in notAllowed:
        if i in string:
            return False

    vowelCounter = 0
    for c in string:
        if c in vowels:
            vowelCounter += 1
    if vowelCounter < 3:
        return False

    lastChar = ''
    foundTwice = False
    for i in range(len(string)):
        if i > 0 and string[i] == lastChar:
            foundTwice = True
        lastChar = string[i]

    return foundTwice


def main():
    rawlines = list()

    with open('./day_5/input.txt', 'r') as f:
        rawlines = f.readlines()

    niceStringCounter = 0
    for line in rawlines:
        if checkNice(line):
            niceStringCounter += 1

    print(niceStringCounter)


if __name__ == '__main__':
    main()
