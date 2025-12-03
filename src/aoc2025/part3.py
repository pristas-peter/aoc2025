def parse(input):
    return input.split('\n')

def get_max_digit_index(digits, start, end):
    last = digits[start]
    result = start

    for i in range(start + 1, end + 1):
        if int(last) < int(digits[i]):
            result = i
            last = digits[i]

    return result

def get_voltage(digits, count):
    result_string = ''
    start = 0
    end = len(digits) - count

    while len(result_string) != count:
        start = get_max_digit_index(digits, start, end)
        result_string += digits[start]
        start = start + 1
        end = end + 1

    return int(result_string)


def pt1(input):
    batteries = parse(input)
    result = []

    for battery in batteries:
        result.append(get_voltage(battery, 2))

    return sum(result)

def pt2(input):
    batteries = parse(input)
    result = []

    for battery in batteries:
        result.append(get_voltage(battery, 12))

    return sum(result)

def main():
    with open('03.txt', 'r') as f:
        data = f.read()

        print(pt1(data))
        print(pt2(data))

if __name__=="__main__":
    main()
