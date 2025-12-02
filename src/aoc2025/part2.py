def get_ranges(input):
    return [tuple(int(y) for y in x.split('-')) for x in input.split(',')]

def get_invalid_pt1(start, end):
    result = []

    for i in range(start, end + 1):
        digits = str(i)
        pattern = ''

        for l in range(0, len(digits)):
            pattern += digits[l]
            length = len(pattern)
            substring = digits[length:]

            if substring == pattern:
                result.append(i)
                break

    return result

def get_invalid_pt2(start, end):
    result = []

    for i in range(start, end + 1):
        digits = str(i)
        pattern = ''

        for l in range(0, len(digits)):
            pattern += digits[l]
            length = len(pattern)
            substring = digits[length:]

            if len(substring) == 0:
                continue

            replace = substring.replace(pattern, '')

            if replace == '':
                result.append(i)
                break

    return result

def pt1(input):
    ranges = get_ranges(input)
    invalid_by_range = {}

    for r in ranges:
        invalid_by_range[r] = get_invalid_pt1(r[0], r[1])

    return sum(sum(v) for v in invalid_by_range.values())


def pt2(input):
    ranges = get_ranges(input)
    invalid_by_range = {}

    for r in ranges:
        invalid_by_range[r] = get_invalid_pt2(r[0], r[1])

    return sum(sum(v) for v in invalid_by_range.values())


def main():
    with open('02.txt', 'r') as f:
        data = f.read()

        print(pt1(data))
        print(pt2(data))

if __name__=="__main__":
    main()
