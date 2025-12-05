import copy

def parse(input):
    return list(map(lambda line: list(line), input.split('\n')))


def getter(data, x, y):
    if y < 0:
        return None

    if x < 0:
        return None

    try:
        return data[y][x]
    except:
        return None


def can_be_removed(data, x, y):
    tl = getter(data, x - 1, y -1)
    t = getter(data, x, y -1)
    tr = getter(data, x + 1, y - 1)
    l = getter(data, x - 1, y)
    r = getter(data, x + 1, y)
    bl = getter(data, x -1, y + 1)
    b = getter(data, x, y + 1)
    br = getter(data, x +1, y + 1)

    count = 0

    for item in [tl, t, tr, l, r, bl, b, br]:
        if item == '@':
            count += 1

    if count < 4:
        return True

    return False

def pt1(input):
    data = parse(input)
    result = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '.':
                continue

            if can_be_removed(data, x, y):
                result += 1

    return result



def pt2(input):
    data = parse(input)
    result = 0


    while True:
        new_data = copy.deepcopy(data)
        did_remove = False

        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '.':
                    continue

                if can_be_removed(data, x, y):
                    result += 1
                    did_remove = True
                    new_data[y][x] = '.'

        if not did_remove:
            break

        data = new_data

    return result

def main():
    with open('04.txt', 'r') as f:
        data = f.read()

        print(pt1(data))
        print(pt2(data))


if __name__ == "__main__":
    main()
