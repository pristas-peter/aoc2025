class Dial:
    def __init__(self):
        self.current = 50

    def left(self):
        self.current -= 1

        if self.current == -1:
            self.current = 99

    def right(self):
        self.current += 1

        if self.current == 100:
            self.current = 0

def parse(data):
    result = []

    for line in data.split('\n'):
        result.append((line[0], int(line[1:])))

    return result


def pt1(input):
    dial = Dial()
    data = parse(input)

    result = 0

    for (direction, count) in data:

        for i in range(0, count):
            if direction == 'L':
                dial.left()

            if direction == 'R':
                dial.right()

        if dial.current == 0:
            result += 1


    return result

def pt2(input):
    data = parse(input)
    dial = Dial()

    result = 0

    for (direction, count) in data:
        for i in range(0, count):
            if direction == 'L':
                dial.left()

            if direction == 'R':
                dial.right()

            if dial.current == 0:
                result += 1


    return result


def main():
    with open('01.txt', 'r') as f:
        data = f.read()

        print(pt1(data))
        print(pt2(data))

if __name__=="__main__":
    main()
